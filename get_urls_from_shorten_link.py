import requests

def get_redirected_urls(shorten_link):
    redirected_urls = []
    response = requests.get(shorten_link, allow_redirects=False)

    while response.status_code // 100 == 3:  # Redirection status codes
        redirected_urls.append(response.headers['Location'])
        response = requests.get(response.headers['Location'], allow_redirects=False)

    return redirected_urls

# Example usage
shorten_link = 'https://lnkd.in/dr3BMArr'
redirected_urls = get_redirected_urls(shorten_link)
print(redirected_urls)

