import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:compest_artificialifelse/api/kepribadian/soal_respon.dart';

const baseUrl = "https://flask-api-compfest.herokuapp.com/api/v1/";

class Api {
  static Future<SoalRespon> getSoal() async {
    var url = baseUrl + "personality/get_questions";
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      print(response.body);
      return SoalRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to get list soal";
    }
  }
}
