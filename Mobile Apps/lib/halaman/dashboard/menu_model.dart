class Category {
  Category({
    this.title = '',
    this.imagePath = '',
    this.lessonCount = 0,
    this.money = 0,
    this.rating = 0.0,
  });

  String title;
  int lessonCount;
  int money;
  double rating;
  String imagePath;

  static List<Category> popularCourseList = <Category>[
    Category(
      imagePath: 'assets/design_course/interFace3.png',
      title: 'Tes Kepribadian',
      lessonCount: 12,
      money: 25,
      rating: 4.8,
    ),
    Category(
      imagePath: 'assets/design_course/interFace4.png',
      title: 'Prediksi Kelulusan',
      lessonCount: 28,
      money: 208,
      rating: 4.9,
    ),
    Category(
      imagePath: 'assets/design_course/interFace3.png',
      title: 'Klasifikasi Paper',
      lessonCount: 12,
      money: 25,
      rating: 4.8,
    ),
    Category(
      imagePath: 'assets/design_course/interFace4.png',
      title: 'Kepribadian Dari Sosmed',
      lessonCount: 28,
      money: 208,
      rating: 4.9,
    ),
  ];
}
