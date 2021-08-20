class Data {
  String s1;
  String s2;
  String s3;
  String s4;
  String s5;
  String s6;
  String s7;
  String s8;
  String s9;
  String s10;
  String s11;
  String s12;
  String s13;
  String s14;
  String s15;
  String s16;
  String s17;
  String s18;
  String s19;
  String s20;
  String s21;
  String s22;
  String s23;
  String s24;
  String s25;
  String s26;
  String s27;
  String s28;
  String s29;
  String s30;
  String s31;
  String s32;
  String s33;
  String s34;
  String s35;
  String s36;
  String s37;
  String s38;
  String s39;
  String s40;
  String s41;
  String s42;
  String s43;
  String s44;
  String s45;
  String s46;
  String s47;
  String s48;
  String s49;
  String s50;

  Data.fromJsonMap(Map<String, dynamic> json)
      : s1 = json['1'],
        s2 = json['2'],
        s3 = json['3'],
        s4 = json['4'],
        s5 = json['5'],
        s6 = json['6'],
        s7 = json['7'],
        s8 = json['8'],
        s9 = json['9'],
        s10 = json['10'],
        s11 = json['11'],
        s12 = json['12'],
        s13 = json['13'],
        s14 = json['14'],
        s15 = json['15'],
        s16 = json['16'],
        s17 = json['17'],
        s18 = json['18'],
        s19 = json['19'],
        s20 = json['20'],
        s21 = json['21'],
        s22 = json['22'],
        s23 = json['23'],
        s24 = json['24'],
        s25 = json['25'],
        s26 = json['26'],
        s27 = json['27'],
        s28 = json['28'],
        s29 = json['29'],
        s30 = json['30'],
        s31 = json['31'],
        s32 = json['32'],
        s33 = json['33'],
        s34 = json['34'],
        s35 = json['35'],
        s36 = json['36'],
        s37 = json['37'],
        s38 = json['38'],
        s39 = json['39'],
        s40 = json['40'],
        s41 = json['41'],
        s42 = json['42'],
        s43 = json['43'],
        s44 = json['44'],
        s45 = json['45'],
        s46 = json['46'],
        s47 = json['47'],
        s48 = json['48'],
        s49 = json['49'],
        s50 = json['50'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['1'] = this.s1;
    data['2'] = this.s2;
    data['3'] = this.s3;
    data['4'] = this.s4;
    data['5'] = this.s5;
    data['6'] = this.s6;
    data['7'] = this.s7;
    data['8'] = this.s8;
    data['9'] = this.s9;
    data['10'] = this.s10;
    data['11'] = this.s11;
    data['12'] = this.s12;
    data['13'] = this.s13;
    data['14'] = this.s14;
    data['15'] = this.s15;
    data['16'] = this.s16;
    data['17'] = this.s17;
    data['18'] = this.s18;
    data['19'] = this.s19;
    data['20'] = this.s20;
    data['21'] = this.s21;
    data['22'] = this.s22;
    data['23'] = this.s23;
    data['24'] = this.s24;
    data['25'] = this.s25;
    data['26'] = this.s26;
    data['27'] = this.s27;
    data['28'] = this.s28;
    data['29'] = this.s29;
    data['30'] = this.s30;
    data['31'] = this.s31;
    data['32'] = this.s32;
    data['33'] = this.s33;
    data['34'] = this.s34;
    data['35'] = this.s35;
    data['36'] = this.s36;
    data['37'] = this.s37;
    data['38'] = this.s38;
    data['39'] = this.s39;
    data['40'] = this.s40;
    data['41'] = this.s41;
    data['42'] = this.s42;
    data['43'] = this.s43;
    data['44'] = this.s44;
    data['45'] = this.s45;
    data['46'] = this.s46;
    data['47'] = this.s47;
    data['48'] = this.s48;
    data['49'] = this.s49;
    data['50'] = this.s50;
    return data;
  }
}

class Meta {
  String message;
  int responseCode;

  Meta.fromJsonMap(Map<String, dynamic> json)
      : message = json['message'],
        responseCode = json['response_code'];

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['message'] = this.message;
    data['response_code'] = this.responseCode;
    return data;
  }
}
