# 파이썬 종료하기
# 윈도우 IDLE이나 리눅스에서는 ctrl+D 키를 누른다
# 프로그램 명령으로 종료할 때는 sys.exit() 함수를 사용할 수 있다.
import sys
sys.exit()

# SystemExit 예외를 발생시켜서 종료할 수도 있다.
print("test")
raise SystemExit
print("test")
