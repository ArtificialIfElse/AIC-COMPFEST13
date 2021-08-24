class JurnalRespon {
  String message;
  int responseCode;
  bool status;
  String theme;

  JurnalRespon.fromJsonMap(Map<String, dynamic> json)
      : message = json['message'],
        responseCode = json['response_code'],
        status = json['status'],
        theme = json['theme'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['message'] = this.message;
    data['response_code'] = this.responseCode;
    data['status'] = this.status;
    data['theme'] = this.theme;
    return data;
  }
}
