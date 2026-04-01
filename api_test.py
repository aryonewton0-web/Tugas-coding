import urllib.request
import json
def test_api():
    url="https://jsonplaceholder.typicode.com/posts"
    try:
        print("Research API Connection... ")
        response=urllib.request.urlopen (url, timeout=1)
        data_json=response.read().decode('utf-8')
        data=json.loads(data_json)
        print("API DATA COLLECTED ☆(ﾉ◕ヮ◕)ﾉ*")
        print("3 Title Displayed:\n")
        for i, post in enumerate(data[:3],start=1):
            print (f" {i},{post['title']}")
    except urllib.error.HTTPError as e:
        print(f" HTTP Error: {e.code}-{e.reason}")
    except urllib.error.URLError as e:
        print(f" URL Error: {e.reason}")
    except exception as e:
        print(f" Unexpected Error: {e}")
if __name__ == "__main__":
    test_api()