class KelulusanRespon {
  String message;
  String prediction;
  int responseCode;
  bool status;

  KelulusanRespon.fromJsonMap(Map<String, dynamic> json)
      : message = json['message'],
        prediction = json['prediction'],
        responseCode = json['response_code'],
        status = json['status'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['message'] = this.message;
    data['prediction'] = this.prediction;
    data['response_code'] = this.responseCode;
    data['status'] = this.status;
    return data;
  }
}
