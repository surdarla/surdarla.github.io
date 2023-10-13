
function solution(phone_book: string[]): boolean {
    let answer: boolean = true;
    const phoneSet: Set<string> = new Set();

    for (let i = 0; i < phone_book.length; i++) {
        const phone: string = phone_book[i];

        // 전화번호를 해시셋에 추가
        phoneSet.add(phone);

        // 각 전화번호의 모든 접두사를 검사
        for (let j = 1; j < phone.length; j++) {
            const prefix: string = phone.slice(0, j);

            // 접두사가 해시셋에 이미 존재하면 중복이므로 false 반환
            if (phoneSet.has(prefix)) {
                answer = false;
                return answer;
            }
        }
    }

    return answer;
}
// 함수 호출 예제
const input: string[] = ["119", "97674223", "1195524421"];
const result: boolean = solution(input);

console.log(result); // true 또는 false 값을 출력
