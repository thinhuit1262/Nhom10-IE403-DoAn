from flask import Flask, request, render_template
from joblib import load
from transformers import pipeline

app = Flask(__name__)

# Mapping 0/1 sang MBTI
AXIS_MAP = {
    'IE': {0: 'I', 1: 'E'},
    'NS': {0: 'N', 1: 'S'},
    'TF': {0: 'T', 1: 'F'},
    'JP': {0: 'J', 1: 'P'},
}

def axes_to_mbti(result_axes):
    return ''.join([
        AXIS_MAP['IE'][result_axes['IE']],
        AXIS_MAP['NS'][result_axes['NS']],
        AXIS_MAP['TF'][result_axes['TF']],
        AXIS_MAP['JP'][result_axes['JP']],
    ])

# Load mô hình .pkl
models = {}
for axis in ['IE', 'JP', 'NS', 'TF']:
    try:
        models[axis] = load(f'pipeline_{axis}.pkl')
    except Exception as e:
        print(f"Lỗi khi load model {axis}: {e}")
        models[axis] = None

# Load Hugging Face MBTI model
try:
    mbti_ai_model = pipeline("text-classification", model="nmcahill/mbti-classifier")
except Exception as e:
    print("Không thể tải mô hình Hugging Face:", e)
    mbti_ai_model = None

def predict_mbti_ai(text):
    if mbti_ai_model:
        try:
            result = mbti_ai_model(text)[0]
            return result['label']
        except Exception:
            return None
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result_axes = {}
    mbti_local = None
    ai_mbti = None
    errors = []

    if request.method == 'POST':
        user_input = request.form.get('text', '').strip()

        # Dự đoán bằng mô hình .pkl
        for axis, model in models.items():
            if model:
                try:
                    result_axes[axis] = int(model.predict([user_input])[0])
                except Exception as e:
                    result_axes[axis] = f"Lỗi: {str(e)}"
                    errors.append(f"{axis} lỗi: {str(e)}")
            else:
                result_axes[axis] = "Model thiếu"
                errors.append(f"{axis} chưa được tải")

        # Ghép thành MBTI
        if all(axis in result_axes and result_axes[axis] in [0, 1] for axis in ['IE', 'NS', 'TF', 'JP']):
            mbti_local = axes_to_mbti(result_axes)

        # Dự đoán bằng Hugging Face
        ai_mbti = predict_mbti_ai(user_input)

    return render_template('index.html',
                           result=result_axes,
                           mbti_local=mbti_local,
                           ai_mbti=ai_mbti,
                           errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
