import requests

def get_github_zen():
    """جلب حكمة عشوائية من واجهة GitHub الرسمية."""
    url = "https://api.github.com/zen"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # التحقق من نجاح الطلب
        # النص العادي (ليس JSON)
        print("💡 حكمة اليوم من GitHub:")
        print(response.text)
    except requests.RequestException as e:
        print(f"حدث خطأ أثناء الاتصال بـ GitHub: {e}")

if __name__ == "__main__":
    get_github_zen()
