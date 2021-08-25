import 'package:compest_artificialifelse/api/jurnal/jurnal_respon.dart';
import 'package:compest_artificialifelse/api/kepribadian/kepribadian_respon.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:compest_artificialifelse/api/kepribadian/soal_respon.dart';
import 'package:compest_artificialifelse/api/kelulusan/kelulusan_respon.dart';

const baseUrl =
    "https://aic-compfest-artificialifelse.as.r.appspot.com/api/v1/";

class Api {
  static Future<SoalRespon> getSoal() async {
    var url = baseUrl + "personality/get_questions";
    final response = await http.get(
      Uri.parse(url),
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
        "Access-Control-Allow-Methods": "GET, POST",
      },
    );
    if (response.statusCode == 200) {
      return SoalRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to get list soal";
    }
  }

  //Diploma

  static Future<KelulusanRespon> cekDiplomaTiga(
      double s1, double s2, double s3) async {
    var url = baseUrl + "graduation/diploma/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print("berhasil");
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  static Future<KelulusanRespon> cekDiplomaEmpat(
      double s1, double s2, double s3, double s4) async {
    var url = baseUrl + "graduation/diploma/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3, s4]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  static Future<KelulusanRespon> cekDiplomaLima(
      double s1, double s2, double s3, double s4, double s5) async {
    var url = baseUrl + "graduation/diploma/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3, s4, s5]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  //Sarjana

  static Future<KelulusanRespon> cekSarjanaLima(
      double s1, double s2, double s3, double s4, double s5) async {
    var url = baseUrl + "graduation/bachelor/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3, s4, s5]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print("berhasil");
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  static Future<KelulusanRespon> cekSarjanaEnam(
      double s1, double s2, double s3, double s4, double s5, double s6) async {
    var url = baseUrl + "graduation/bachelor/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3, s4, s5, s6]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  static Future<KelulusanRespon> cekSarjanaTujuh(double s1, double s2,
      double s3, double s4, double s5, double s6, double s7) async {
    var url = baseUrl + "graduation/bachelor/predict";
    String body = json.encode({
      "nilai": [s1, s2, s3, s4, s5, s6, s7]
    });
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return KelulusanRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  //Prediksi Kperibadian
  static Future<KepribadianRespon> cekKepribadian(List<double> jawaban) async {
    var url = baseUrl + "personality/predict";
    String body = json.encode({"answer": jawaban});
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return KepribadianRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }

  //Prediksi Kperibadian
  static Future<JurnalRespon> cekJurnal(
      String judul, String abstrak, int bahasa) async {
    var url = baseUrl + "paper/predict";
    String body =
        json.encode({"title": judul, "abstract": abstrak, "language": bahasa});
    final response = await http.post(Uri.parse(url),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
          "Access-Control-Allow-Methods": "GET, POST",
        },
        body: body);
    if (response.statusCode == 200) {
      print(response.body);
      return JurnalRespon.fromJsonMap(jsonDecode(response.body));
    } else {
      throw "failed to connect server";
    }
  }
}
