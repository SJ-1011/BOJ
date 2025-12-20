# 나라 정보를 저장할 클래스 정의
class Country:
    def __init__(self, num, gold, silver, bronze):
        self.num = num
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

# 메인 함수
def main():
    n, k = map(int, input().split())
    countries = []

    # 나라 정보 입력 받기
    for _ in range(n):
        num, gold, silver, bronze = map(int, input().split())
        countries.append(Country(num, gold, silver, bronze))

    # 정렬 기준 함수 정의
    def sort_key(country):
        return (country.gold, country.silver, country.bronze)

    # 정렬 후 등수 계산
    countries.sort(key=sort_key, reverse=True)
    rank = 1
    for i, country in enumerate(countries):
        if country.num == k:
            print(rank)
            break
        if i > 0 and (country.gold, country.silver, country.bronze) != (countries[i - 1].gold, countries[i - 1].silver, countries[i - 1].bronze):
            rank = i + 1

if __name__ == "__main__":
    main()
