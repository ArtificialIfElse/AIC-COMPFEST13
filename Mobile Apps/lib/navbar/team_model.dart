import 'package:flutter/material.dart';

class Team {
  Team({
    this.nama = '',
    this.role = '',
    this.ket = '',
    this.quote = '',
    this.foto1 = '',
    this.foto2 = '',
    this.warna = 0,
  });

  String nama;
  String role;
  String ket;
  String quote;
  String foto1;
  String foto2;
  int warna;

  static List<Team> namaTeam = <Team>[
    Team(
      nama: 'Muhammad Novrizal Ghiffari',
      role: 'Mobile Developer',
      ket: '+62 878-6338-8912\nrizal.novrizal999@gmail.com\n@zazal_ghiffari',
      quote:
          '"Suka aja bermimpi. 2023 bakal keliling indonesia! 2028 bakal keliling dunia!"',
      foto1: 'assets/328918923.png',
      foto2: 'assets/775870730.png',
      warna: 0xff5858ff,
    ),
    Team(
      nama: 'Handhika Yanuar Pratama',
      role: 'AI/ML Developer',
      ket: '+62 812-2590-0513\nhandhikayp@gmail.com\n@handhikayp',
      quote: '"When Possibilities Meet Technology"',
      foto1: 'assets/1298391023.png',
      foto2: 'assets/71202864.png',
      warna: 0xff00c66e,
    ),
    Team(
      nama: 'Yosep Novento Nugroho',
      role: 'Backend Developer',
      ket: '+62 818-0992-9885\nyosepnoventon@gmail.com\n@ventodeco',
      quote: '"Learning by doing!"',
      foto1: 'assets/620936020.png',
      foto2: 'assets/1617374318680.png',
      warna: 0xffe23d37,
    ),
  ];
}
