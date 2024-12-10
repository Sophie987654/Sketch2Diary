# Sketch2Diary

# 끄적끄적 (Sketch Sketch) - AI 기반 어린이 일기 앱

## 소개

**끄적끄적**은 어린이들이 그림과 이야기로 일기를 작성할 수 있도록 돕는 AI 기반의 애플리케이션입니다. 이 앱은 어린이가 자신의 일상을 그림과 이야기로 기록하며 감정 표현을 촉진하고, 그 과정을 통해 부모가 자녀의 정신 건강 상태를 파악할 수 있도록 돕습니다. **끄적끄적**은 어린이의 그림과 이야기를 분석해 일기 형식으로 정리해주는 서비스를 제공합니다.

## 목적

본 프로젝트는 어린이들이 일기 작성에 대한 저항을 줄이고 창의적이고 재미있는 방식으로 일기 쓰기를 장려하기 위해 개발되었습니다. 텍스트와 이미지 기반의 기록을 결합하여, 어린이들이 일상에서 느낀 감정과 경험을 AI가 분석하고 정리하는 기능을 제공합니다.

## 주요 기능

- **음성 인식 (STT)**: 어린이가 말하는 이야기를 텍스트로 변환합니다.
- **그림 인식 및 분석**: 어린이가 그린 그림을 AI가 인식하고 감정을 분석하여 텍스트로 변환합니다.
- **일기 생성**: 어린이의 이야기를 바탕으로 일기를 자동으로 작성합니다.
- **감정 분석**: AI가 어린이의 그림을 분석하여 감정 상태를 파악합니다.
- **챗봇 (LangChain 기반)**: 어린이가 그린 그림과 음성에 대한 대화를 진행할 수 있는 챗봇을 제공합니다. 챗봇은 사용자의 입력에 따라 친절하고 자연스럽게 대화를 이어가며, 그림에 대한 질문을 유도하거나 대화를 요약해줍니다. 
  - `LangChain` 라이브러리를 활용하여 다양한 대화 흐름을 관리하며, OpenAI GPT-3.5를 통해 사용자에게 맞춤형 대답을 제공합니다.
  - 챗봇은 어린이가 그린 그림에 대해 이야기하고, 해당 그림에서 나타나는 감정이나 메시지를 파악하여 대화를 진행합니다.

## 사용 기술

- **음성 인식 (STT)**: 어린이의 음성을 텍스트로 변환하는 **구글 STT** 모델을 사용합니다.
- **객체 인식**: YOLOv8 모델을 사용하여 어린이의 그림에서 객체를 인식하고 분석합니다.
- **자연어 처리 (NLP)**: GPT-3.5-turbo를 사용하여 음성과 그림을 기반으로 일기를 생성합니다.
- **백엔드**: Flask API를 사용하여 요청을 처리하고 AI 모델과 통합합니다.
- **프론트엔드**: 안드로이드 애플리케이션은 Jetpack Compose를 사용하여 매끄러운 사용자 경험을 제공합니다.

## 데이터셋

**AI 기반 어린이 미술치료 진단 데이터셋**(aihub)을 사용하여 객체 인식 모델을 훈련시켰습니다. 이 데이터셋은 어린이의 그림을 대상으로 하며, 감정 분석 및 객체 인식을 위해 사용됩니다.

- **데이터 수집**: 7-13세 어린이 7,000명
- **데이터 구조**: 56,000개의 이미지와 해당하는 객체 인식 라벨
- **훈련 및 검증**: 각 클래스별로 500개의 훈련 이미지와 100개의 검증 이미지

## 데이터셋 구조

이 프로젝트는 이미지 분류를 위한 데이터셋을 사용합니다. 데이터셋은 **Training**과 **Validation** 폴더로 나뉘며, 각 폴더는 이미지와 라벨로 구성됩니다.

### Training 데이터

- `images/`
  - `tree/` (500 이미지)
  - `man/` (500 이미지)
  - `woman/` (500 이미지)
  - `house/` (500 이미지)
  
- `labels/`
  - `tree/` (500 라벨)
  - `man/` (500 라벨)
  - `woman/` (500 라벨)
  - `house/` (500 라벨)

### Validation 데이터

- `images/`
  - `tree/` (100 이미지)
  - `man/` (100 이미지)
  - `woman/` (100 이미지)
  - `house/` (100 이미지)
  
- `labels/`
  - `tree/` (100 라벨)
  - `man/` (100 라벨)
  - `woman/` (100 라벨)
  - `house/` (100 라벨)
