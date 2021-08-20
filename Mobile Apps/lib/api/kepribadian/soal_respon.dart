import 'package:compest_artificialifelse/api/kepribadian/soal.dart';

class SoalRespon {
  List<Data> data;
  List<Meta> meta;
  bool status;

  SoalRespon.fromJsonMap(Map<String, dynamic> json)
      : data = List<Data>.from(json["data"].map((it) => Data.fromJsonMap(it))),
        meta = List<Meta>.from(json["meta"].map((it) => Meta.fromJsonMap(it))),
        status = json['status'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['data'] =
        data != null ? this.data.map((v) => v.toJson()).toList() : null;
    data['meta'] =
        data != null ? this.meta.map((v) => v.toJson()).toList() : null;
    data['status'] = this.status;
    return data;
  }
}
