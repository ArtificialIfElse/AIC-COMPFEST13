class SoalRespon {
  List<Data> data;
  String message;
  int responseCode;
  bool status;

  SoalRespon.fromJsonMap(Map<String, dynamic> json)
      : data = List<Data>.from(json["data"].map((it) => Data.fromJsonMap(it))),
        message = json['message'],
        responseCode = json['response_code'],
        status = json['status'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['data'] =
        data != null ? this.data.map((v) => v.toJson()).toList() : null;
    data['message'] = this.message;
    data['response_code'] = this.responseCode;
    data['status'] = this.status;
    return data;
  }
}

class Data {
  String namaSoal;
  String soal;
  double value_slider;

  Data.fromJsonMap(Map<String, dynamic> json)
      : namaSoal = json['nama_soal'],
        soal = json['soal'],
        value_slider = json['value_slider'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['nama_soal'] = this.namaSoal;
    data['soal'] = this.soal;
    data['value_slider'] = this.value_slider;
    return data;
  }
}
