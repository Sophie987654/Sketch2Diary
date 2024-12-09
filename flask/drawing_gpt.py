from flask import Flask, request, jsonify, redirect, url_for
import openai, time

app = Flask(__name__)

# 객체 4개 목록은 초반에 return 되어 클라이언트에서 관리된다고 가정
# 클라이언트에서 질문 키워드를 넘겨줌
# 주고 받은 내용 한 번에 클라 -> 백 전달하여 요약 

# OpenAI API 키 설정


@app.route('/api/chat/system', methods=['POST'])
def from_system():
    data = request.json
    issue = data.get('input_issue')

    # 대화 내용을 포함한 템플릿 생성
    prompt = f"너는 친절한 챗봇이야. 어린이가 그린 그림을 보고, 그 그림에 대해 자연스럽게 질문을 해줘. 아이가 그림을 그린 이유와 그 그림에 담긴 생각을 들을 수 있도록 유도하고, 그림에 나타난 색깔, 형태, 그리고 그리면서 느낀 점에 대해 이야기하도록 해. 질문을 할 때는 아이가 자유롭게 표현할 수 있도록 도와주고, 긍정적인 피드백을 제공해줘. 예를 들면, '와! 이 그림 정말 멋져! 이 그림 속에서 어떤 이야기를 담고 싶은지 궁금해.' 이렇게 물어봐줘. 욕설이나 부정적인 표현은 절대로 사용하지 않도록 해."

    # OpenAI API를 사용하여 대화 요약
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5,
        max_tokens=100
    )

    # 요약된 내용을 클라이언트에게 반환합니다.
    return jsonify({"system": response.choices[0].message['content'].strip()}), 200



@app.route('/api/chat/kid', methods=['POST'])
def from_kid():
    data = request.json
    system = data.get('system')
    conversation = data.get('conversation')


    # 대화 내용을 포함한 템플릿 생성
    prompt = f"대화 내용: {system}에 대해 {conversation} 이렇게 답장했는데, 아이가 쉽게 이해할 수 있도록 그림일기 형식으로 요약해줘. 요약할 때는 '오늘', '누가', '어디서', '뭐를', '왜', '어떻게'의 육하원칙을 사용해서 간단하고 친절하게 설명해줘. 아이가 이해하기 쉽도록 재밌고 친근하게 말해줘. 너무 어려운 단어는 피하고, 필요한 경우 쉬운 예시나 비유를 들어줘. 욕설이나 부정적인 표현은 절대로 사용하지 않도록 해."


    # OpenAI API를 사용하여 대화 요약
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
                {"role": "user", "content": conversation}],
        temperature=0.5,
        max_tokens=100
    )
    summary = response.choices[0].message['content'].strip()
    return jsonify({"summary": summary}), 200



if __name__ == '__main__':
    app.run(host='192.168.56.1', port=5000)
