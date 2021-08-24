class KepribadianRespon {
  List<String> advice;
  double agreeableness;
  double conscientiousness;
  double extroversion;
  String mbti;
  String message;
  double neuroticism;
  double openness;
  String recommendationMajor;
  int responseCode;
  bool status;

  KepribadianRespon.fromJsonMap(Map<String, dynamic> json)
      : advice = json['advice'].cast<String>(),
        agreeableness = json['agreeableness'],
        conscientiousness = json['conscientiousness'],
        extroversion = json['extroversion'],
        mbti = json['mbti'],
        message = json['message'],
        neuroticism = json['neuroticism'],
        openness = json['openness'],
        recommendationMajor = json['recommendation_major'],
        responseCode = json['response_code'],
        status = json['status'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['advice'] = this.advice;
    data['agreeableness'] = this.agreeableness;
    data['conscientiousness'] = this.conscientiousness;
    data['extroversion'] = this.extroversion;
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
