from joblib import load
import pickle

def check(path):
    print(f"\n🔍 Checking: {path}")
    try:
        with open(path, 'rb') as f:
            model = pickle.load(f)
        print("✅ Loaded with pickle")
    except Exception as e:
        print(f"❌ Pickle failed: {e}")
    
    try:
        model = load(path)
        print("✅ Loaded with joblib")
    except Exception as e:
        print(f"❌ Joblib failed: {e}")

for axis in ['IE', 'JP', 'NS', 'TF']:
    check(f'pipeline_{axis}.pkl')
