class KepribadianRespon {
  List<String> advice;
  int agreeableness;
  int conscientiousness;
  int extroversion;
  String mbti;
  String message;
  int neuroticism;
  int openness;
  String recommendationMajor;
  int responseCode;
  bool status;

  KepribadianRespon.fromJsonMap(Map<String, dynamic> json)
      : advice = json['advice'].cast<String>(),
        agreeableness = (json['agreeableness'] * 10).toInt(),
        conscientiousness = (json['conscientiousness'] * 10).toInt(),
        extroversion = (json['extroversion'] * 10).toInt(),
        mbti = json['mbti'],
        message = json['message'],
        neuroticism = (json['neuroticism'] * 10).toInt(),
        openness = (json['openness'] * 10).toInt(),
        recommendationMajor = json['recommendation_major'],
        responseCode = json['response_code'],
        status = json['status'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['advice'] = this.advice;
    data['agreeableness'] = this.agreeableness;
    data['conscientiousness'] = this.conscientiousness;
    data['extroversion'] = this.extroversion.toString();
    data['mbti'] = this.mbti;
    data['message'] = this.message;
    data['neuroticism'] = this.neuroticism;
    data['openness'] = this.openness;
    data['recommendation_major'] = this.recommendationMajor;
    data['response_code'] = this.responseCode;
    data['status'] = this.status;
    return data;
  }
}
