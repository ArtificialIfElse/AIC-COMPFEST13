import 'package:flutter/material.dart';
import 'package:slimy_card/slimy_card.dart';
import 'team_model.dart';

class TeamScreen extends StatefulWidget {
  @override
  _TeamScreen createState() => _TeamScreen();
}

class _TeamScreen extends State<TeamScreen> {
  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
      // This streamBuilder reads the real-time status of SlimyCard.
      initialData: false,
      stream: slimyCard.stream, //Stream of SlimyCard
      builder: ((BuildContext context, AsyncSnapshot snapshot) {
        return ListView.builder(
            itemCount: Team.namaTeam.length,
            itemBuilder: (context, index) {
              return Column(
                children: <Widget>[
                  SizedBox(height: 100),
                  SlimyCard(
                    color: Color(Team.namaTeam[index].warna),
                    topCardWidget: topCardWidget(
                        (snapshot.data)
                            ? Team.namaTeam[index].foto1
                            : Team.namaTeam[index].foto2,
                        Team.namaTeam[index].nama,
                        Team.namaTeam[index].role,
                        Team.namaTeam[index].ket),
                    bottomCardWidget:
                        bottomCardWidget(Team.namaTeam[index].quote),
                  ),
                  Team.namaTeam.length == index + 1
                      ? SizedBox(
                          height: 36,
                        )
                      : SizedBox(),
                ],
              );
            });
      }),
    );
  }

  Widget topCardWidget(String imagePath, String nama, String role, String ket) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Container(
          height: 70,
          width: 70,
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(15),
            image: DecorationImage(image: AssetImage(imagePath)),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.1),
                blurRadius: 20,
                spreadRadius: 1,
              ),
            ],
          ),
        ),
        SizedBox(height: 15),
        Text(
          nama,
          style: TextStyle(color: Colors.white, fontSize: 20),
        ),
        Text(
          role,
          style: TextStyle(
              color: Colors.white, fontSize: 14, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 15),
        Text(
          ket,
          style: TextStyle(
              color: Colors.white.withOpacity(0.8),
              fontSize: 12,
              fontWeight: FontWeight.w500),
        ),
        SizedBox(height: 10),
      ],
    );
  }

  // This widget will be passed as Bottom Card's Widget.
  Widget bottomCardWidget(String quote) {
    return Text(
      quote,
      style: TextStyle(
        color: Colors.white,
        fontSize: 12,
        fontWeight: FontWeight.w500,
      ),
      textAlign: TextAlign.center,
    );
  }
}
