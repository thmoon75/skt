import re

# 허용 문자 전체에 대한 정규식 패턴
ALLOWED_CHARS_PATTERN = r"^[A-Za-z0-9!@#$%^&*()_\+\-=\[\]{};':\",.<>\/\?]+$"

def validate_password(password: str, user_id: str | None = None):
    errors = []

    # 1) 길이 체크
    if not (10 <= len(password) <= 64):
        errors.append("비밀번호는 10자 이상 64자 이하여야 합니다.")

    # 2) 허용 문자 검사
    if not re.match(ALLOWED_CHARS_PATTERN, password):
        errors.append("허용되지 않은 문자가 포함되어 있습니다. (공백 사용 불가)")

    # 3) 문자 종류 검사
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*()_\+\-=\[\]{};':\",.<>\/\?]", password))

    categories_count = sum([has_upper, has_lower, has_digit, has_special])
    if categories_count < 3:
        errors.append(
            "다음 중 최소 3가지 종류를 포함해야 합니다: 대문자, 소문자, 숫자, 특수문자"
        )

    # 4) 동일 문자 3회 이상 연속 금지
    if re.search(r"(.)\1\1", password):
        errors.append("같은 문자를 3번 이상 연속 사용할 수 없습니다.")

    # 5) 아이디 포함 금지
    if user_id and user_id.lower() in password.lower():
        errors.append("비밀번호에 아이디를 포함할 수 없습니다.")

    # 6) 간단한 블랙리스트
    common_passwords = {
        "password", "123456", "qwerty", "111111", "123456789", "abc123"
    }
    if password.lower() in common_passwords:
        errors.append("너무 흔한 비밀번호입니다. 다른 비밀번호를 사용해주세요.")

    is_valid = len(errors) == 0
    return is_valid, errors


# ===========================================
# 반복 실행 + EXIT 종료 기능
# ===========================================
if __name__ == "__main__":
    user_id = "taehee"  # 예시 계정 아이디

    print("🔐 비밀번호 검증 프로그램")
    print("종료하려면 'EXIT'을 입력하세요.\n")

    while True:
        password = input("검증할 비밀번호를 입력하세요: ")

        # 종료 조건
        if password.upper() in ["EXIT", "QUIT", "!EXIT"]:
            print("프로그램을 종료합니다.")
            break

        # 비밀번호 검증
        ok, error_list = validate_password(password, user_id=user_id)

        if ok:
            print("✅ 사용 가능한 비밀번호입니다!\n")
        else:
            print("❌ 비밀번호가 규칙에 맞지 않습니다:")
            for e in error_list:
                print(" -", e)
            print()
