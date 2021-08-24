import 'package:flutter/material.dart';
import 'package:compest_artificialifelse/halaman/dashboard/kelulusan/diploma_page.dart';
import 'package:compest_artificialifelse/halaman/dashboard/kelulusan/bachelor_page.dart';

class MenuKelulusan extends StatefulWidget {
  MenuKelulusan({Key? key}) : super(key: key);

  @override
  _MenuKelulusan createState() => _MenuKelulusan();
}

class _MenuKelulusan extends State<MenuKelulusan> {
  int _seletedItem = 0;
  var _pages = [DiplomaPage(), BachelorPage()];
  var _pageController = PageController();
  bool result = true;

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBody: true,
      backgroundColor: Colors.transparent,
      body: PageView(
        //scrollDirection: Axis.vertical,
        children: _pages,
        onPageChanged: (index) {
          setState(() {
            _seletedItem = index;
          });
        },
        controller: _pageController,
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(30.0),
        child: Container(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.only(
                  topRight: Radius.circular(100),
                  topLeft: Radius.circular(100),
                  bottomLeft: Radius.circular(100),
                  bottomRight: Radius.circular(100)),
              boxShadow: [
                BoxShadow(
                    color: Colors.black38, spreadRadius: 0, blurRadius: 10),
              ],
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(100.0),
                  topRight: Radius.circular(100.0),
                  bottomLeft: Radius.circular(100),
                  bottomRight: Radius.circular(100)),
              child: BottomNavigationBar(
                selectedItemColor: Color(0xff27C499),
                unselectedItemColor: Colors.grey[500],
                items: [
                  // ignore: deprecated_member_use
                  BottomNavigationBarItem(
                      // ignore: deprecated_member_use
                      icon: Icon(Icons.school),
                      // ignore: deprecated_member_use
                      title: Text('Diploma')),
                  BottomNavigationBarItem(
                      // ignore: deprecated_member_use
                      icon: Icon(Icons.account_balance),
                      // ignore: deprecated_member_use
                      title: Text('Bachelor')),
                ],
                currentIndex: _seletedItem,
                onTap: (index) {
                  setState(() {
                    _seletedItem = index;
                    _pageController.animateToPage(_seletedItem,
                        duration: Duration(milliseconds: 200),
                        curve: Curves.linear);
                  });
                },
              ),
            )),
      ),
    );
  }
}
