import 'package:flutter/material.dart';
import 'package:compest_artificialifelse/halaman/splash/introduction_animation_screen.dart';
import 'package:compest_artificialifelse/halaman/dashboard/menu_card.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Compest Artificial If Else',
      home: IntroductionAnimationScreen(),
    );
  }
}
