import requests
import time

# List of APIs / websites to check
urls = [
    "https://www.google.com",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://thisurldoesnotexist.xyz"
]

def check_api(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()

        status = "🟢 UP" if response.status_code == 200 else "🟡 ISSUE"
        response_time = round((end - start) * 1000, 2)

        print(f"{url}")
        print(f"Status: {status}")
        print(f"Response Time: {response_time} ms\n")

    except requests.exceptions.RequestException:
        print(f"{url}")
        print("Status: 🔴 DOWN")
        print("Response Time: Timeout/Error\n")


print("\n🌐 API Health Checker\n" + "-"*30)

for url in urls:
    check_api(url)

print("✅ Check Completed\n")