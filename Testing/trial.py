from urllib.request import urlopen
from bs4 import BeautifulSoup

def print_secret_message(url):
    html = urlopen(url).read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")

    points = []

    for row in soup.find_all("tr"):
        cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]

        if len(cols) != 3:
            continue

        try:
            x = int(cols[0])
            char = cols[1]
            y = int(cols[2])

            points.append((x, y, char))
        except ValueError:
            pass

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, y, _ in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    # IMPORTANT: print from highest y to lowest y
    for row in reversed(grid):
        print("".join(row))


print_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)