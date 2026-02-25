from joblib import load
from transformers import pipeline

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
        print(f"Không load được model {axis}: {e}")
        models[axis] = None

# Load Hugging Face MBTI model (miễn phí)
try:
    mbti_model = pipeline("text-classification", model="nmcahill/mbti-classifier")
except Exception as e:
    print("Không thể tải mô hình Hugging Face:", e)
    mbti_model = None

# Nhập văn bản
text = input("Nhập đoạn văn thể hiện tính cách của bạn:\n")

# Dự đoán bằng mô hình .pkl
result_axes = {}
for axis, model in models.items():
    if model:
        result_axes[axis] = int(model.predict([text])[0])

mbti_local = axes_to_mbti(result_axes)

# Dự đoán bằng Hugging Face
if mbti_model:
    ai_result = mbti_model(text)[0]['label']
else:
    ai_result = "Không thể truy cập mô hình AI"

# In ra kết quả
print("\n--- KẾT QUẢ ---")
print("Mô hình huấn luyện (.pkl):", mbti_local)
print("AI Hugging Face:", ai_result)

if mbti_local == ai_result:
    print("✅ Hai kết quả khớp nhau:", mbti_local)
else:
    print("❌ Hai kết quả KHÔNG khớp:")
    print("   Local model:", mbti_local)
    print("   Hugging Face:", ai_result)
