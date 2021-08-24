class Category {
  Category({
    this.title = '',
    this.imagePath = '',
    this.status = '',
  });

  String title;
  String status;
  String imagePath;

  static List<Category> popularCourseList = <Category>[
    Category(
      imagePath: 'assets/interFace4.png',
      title: 'Tes Kepribadian',
      status: 'mau tau \nkepribadianmu?',
    ),
    Category(
      imagePath: 'assets/interFace3.png',
      title: 'Cek Kelulusan',
      status: 'kamu lulus \nperdikat apa?',
    ),
    Category(
      imagePath: 'assets/interFace1.png',
      title: 'Klasifikasi Paper',
      status: 'bingung sama \ntema paper?',
    ),
    Category(
      imagePath: 'assets/interFace2.png',
      title: 'Kepribadian Dari Sosmed',
      status: 'Cooming Soon',
    ),
  ];
}
