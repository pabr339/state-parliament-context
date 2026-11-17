# Raw data as collected from official / secondary sources (see source columns).
# Semicolon CSV blocks: parsed by build.py
NA = None

SRC = {
 "BE_KAS": "https://downloads.kas.de/wahlen/Wahldaten/Wahlen_in_Berlin.pdf",
 "BE81": "https://en.wikipedia.org/wiki/1981_West_Berlin_state_election",
 "BE85": "https://en.wikipedia.org/wiki/1985_West_Berlin_state_election",
 "BE89": "https://en.wikipedia.org/wiki/1989_West_Berlin_state_election",
 "BE90": "https://en.wikipedia.org/wiki/1990_Berlin_state_election",
 "BE95": "https://en.wikipedia.org/wiki/1995_Berlin_state_election",
 "BE99": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00021700/Landeswahlleiterbericht_AH1999.pdf",
 "BE01": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00021666/Landeswahlleiterbericht_AH2001.pdf",
 "BE06": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00022758/Landeswahlleiterbericht_AH06.pdf",
 "BE11": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00021591/SB_B7-2-3-j05-11_BE.pdf",
 "BE16": "https://www.wahlrecht.de/news/2016/abgeordnetenhauswahl-berlin-2016.html",
 "BE21": "https://www.wahlen-berlin.de/wahlen/BE2021/afspraes/WB/SB_B07-02-03_2021j05_BE.pdf",
 "BE23": "https://download.statistik-berlin-brandenburg.de/538210b8454f4642/99e340a74910/SB_B07-02-03_2023j05_BE.pdf",
 "BE26": "https://download.statistik-berlin-brandenburg.de/870314b4bc23589b/4d38d373adff/SB_B07-02-03_2026j05_BE.pdf",
 "BB90": "https://en.wikipedia.org/wiki/1990_Brandenburg_state_election",
 "BB_KAS": "https://downloads.kas.de/wahlen/Wahldaten/Wahlen_in_Brandenburg.pdf",
 "BB94": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00010765/SB_B7-2-1_5j-04-Vorwahl_BB.pdf",
 "BB04": "https://www.landtag.brandenburg.de/media_fast/6/Handbuch-web.pdf",
 "BB09": "https://www.landtag.brandenburg.de/media_fast/6/Landtag%20HB_web.pdf",
 "BB14": "https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/BBHeft_derivate_00005974/SB_B07-02-03_2014j05_BBa.pdf",
 "BB19": "https://bundeswahlleiterin.de/service/landtagswahlen/land-12.html",
 "BB24": "https://wahlen.brandenburg.de/sixcms/media.php/9/PM_35_%202024%20Endg%C3%BCltiges%20Ergebnis%20LTW%202024.pdf",
 "BW": "https://bundeswahlleiterin.de/dam/jcr/a333e523-0717-42ad-a772-d5ad7e7e97cc/ltw_erg_gesamt.pdf",
 "BW26": "https://bundeswahlleiterin.de/service/landtagswahlen/land-8.html",
}

# state;election_date;election_type;wahlperiode;territory;electorate;voters;turnout_pct_reported;valid_votes;invalid_votes;total_seats;vote_type;src
ELECTIONS = """
BE;1981-05-10;early;9;West Berlin;1514642;1291842;85.3;1262166;NA;132;Zweitstimme;BE81|BE_KAS
BE;1985-03-10;regular;10;West Berlin;NA;1259818;83.6;1245004;NA;144;Zweitstimme;BE85|BE_KAS
BE;1989-01-29;regular;11;West Berlin;1532870;1220423;79.6;1200672;NA;138;Zweitstimme;BE89|BE_KAS
BE;1990-12-02;unification;12;Berlin (unified);NA;NA;80.8;2019198;NA;241;Zweitstimme;BE90|BE_KAS
BE;1995-10-22;regular;13;Berlin (unified);NA;NA;68.6;1669186;NA;206;Zweitstimme;BE95|BE99
BE;1999-10-10;regular;14;Berlin (unified);2414493;1582407;65.5;1563576;17646;169;Zweitstimme;BE99|BE01
BE;2001-10-21;early;15;Berlin (unified);2417574;1645673;68.1;1623338;21359;141;Zweitstimme;BE01
BE;2006-09-17;regular;16;Berlin (unified);2425480;1407754;58.0;1377355;28241;149;Zweitstimme;BE06
BE;2011-09-18;regular;17;Berlin (unified);2469716;1487487;60.2;1461185;23992;149;Zweitstimme;BE11
BE;2016-09-18;regular;18;Berlin (unified);2485379;1662476;66.9;1635169;25694;160;Zweitstimme;BE16
BE;2021-09-26;regular (annulled);19;Berlin (unified);2447600;1844278;75.4;1821664;17865;147;Zweitstimme;BE21
BE;2023-02-12;repeat;19;Berlin (unified);2431776;1529558;62.9;1516860;11039;159;Zweitstimme;BE23
BE;2026-09-20;regular;20;Berlin (unified);2487318;1846344;74.2;1825672;20672;153;Zweitstimme;BE26
BB;1990-10-14;first;1;Brandenburg;1955403;1312120;67.1;1273906;38214;88;Zweitstimme;BB90|BB_KAS
BB;1994-09-11;regular;2;Brandenburg;1933680;1089161;56.33;1072019;17142;88;Zweitstimme;BB94
BB;1999-09-05;regular;3;Brandenburg;2056834;1116874;54.30;1102360;14514;89;Zweitstimme;BB94
BB;2004-09-19;regular;4;Brandenburg;2117145;1194192;56.4;1168909;25283;88;Zweitstimme;BB04
BB;2009-09-27;regular;5;Brandenburg;2126357;1425069;67.0;1388722;36347;88;Zweitstimme;BB09
BB;2014-09-14;regular;6;Brandenburg;2094458;1002753;47.9;987321;15432;88;Zweitstimme;BB14
BB;2019-09-01;regular;7;Brandenburg;2088592;1280895;61.3;1265106;15789;88;Zweitstimme;BB19
BB;2024-09-22;regular;8;Brandenburg;2076920;1513975;72.90;1501619;12356;88;Zweitstimme;BB24
BW;1980-03-16;regular;8;Baden-Württemberg;6319950;4549463;72.0;4513009;36454;124;single vote;BW
BW;1984-03-25;regular;9;Baden-Württemberg;6609204;4706241;71.2;4650186;56055;126;single vote;BW
BW;1988-03-20;regular;10;Baden-Württemberg;6872330;4933846;71.8;4878062;55784;125;single vote;BW
BW;1992-04-05;regular;11;Baden-Württemberg;7154575;5014446;70.1;4949199;65247;146;single vote;BW
BW;1996-03-24;regular;12;Baden-Württemberg;7189906;4859305;67.6;4784129;75176;155;single vote;BW
BW;2001-03-25;regular;13;Baden-Württemberg;7313844;4576943;62.6;4530763;46180;128;single vote;BW
BW;2006-03-26;regular;14;Baden-Württemberg;7516919;4012441;53.4;3960615;51826;139;single vote;BW
BW;2011-03-27;regular;15;Baden-Württemberg;7622873;5051941;66.3;4983719;68222;138;single vote;BW
BW;2016-03-13;regular;16;Baden-Württemberg;7683464;5411945;70.4;5361250;50695;143;single vote;BW
BW;2021-03-14;regular;17;Baden-Württemberg;7671039;4894500;63.8;4859651;34849;154;single vote;BW
BW;2026-03-08;regular;18;Baden-Württemberg;7764858;5406737;69.6;5375109;31628;157;Zweitstimme (new 2-vote system);BW26
"""

# state;election_date;party_label;votes;vote_pct_reported;seats;src
PARTIES = """
BE;1981-05-10;CDU;605265;48.0;65;BE81
BE;1981-05-10;SPD;483778;38.3;51;BE81
BE;1981-05-10;AL;90653;7.2;9;BE81
BE;1981-05-10;FDP;70529;5.6;7;BE81
BE;1981-05-10;SEW;8176;0.6;0;BE81
BE;1981-05-10;Sonstige;3765;0.3;0;BE81
BE;1985-03-10;CDU;577867;46.4;69;BE85
BE;1985-03-10;SPD;402875;32.4;48;BE85
BE;1985-03-10;AL;132484;10.6;15;BE85
BE;1985-03-10;FDP;105209;8.5;12;BE85
BE;1985-03-10;DA (Demokratische Alternative);15857;1.3;0;BE85
BE;1985-03-10;SEW;7731;0.6;0;BE85
BE;1985-03-10;Sonstige;2985;0.2;0;BE85
BE;1989-01-29;CDU;453211;37.7;55;BE89
BE;1989-01-29;SPD;448203;37.3;55;BE89
BE;1989-01-29;AL;141529;11.8;17;BE89
BE;1989-01-29;REP;90222;7.5;11;BE89
BE;1989-01-29;FDP;47153;3.9;0;BE89
BE;1989-01-29;Sonstige;20354;1.7;0;BE_KAS
BE;1990-12-02;CDU;815382;40.4;101;BE90
BE;1990-12-02;SPD;614075;30.4;76;BE90
BE;1990-12-02;PDS;184820;9.2;23;BE90
BE;1990-12-02;FDP;143080;7.1;18;BE90
BE;1990-12-02;GRÜNE/AL;100839;5.0;12;BE90
BE;1990-12-02;Bündnis 90/Grüne/UFV;87891;4.4;11;BE90
BE;1990-12-02;REP;62041;3.1;0;BE90
BE;1990-12-02;Sonstige;11070;0.5;0;BE90
BE;1995-10-22;CDU;625005;37.4;87;BE95
BE;1995-10-22;SPD;393245;23.6;55;BE95
BE;1995-10-22;PDS;244196;14.6;34;BE95
BE;1995-10-22;GRÜNE;219990;13.2;30;BE95
BE;1995-10-22;REP;45462;2.7;0;BE95
BE;1995-10-22;FDP;42391;2.5;0;BE95
BE;1995-10-22;GRAUE;28356;1.7;0;BE95
BE;1995-10-22;Sonstige;70541;4.2;0;BE95
BE;1999-10-10;CDU;637311;40.8;76;BE99
BE;1999-10-10;SPD;349731;22.4;42;BE99
BE;1999-10-10;PDS;276869;17.7;33;BE99
BE;1999-10-10;GRÜNE;155322;9.9;18;BE99
BE;1999-10-10;REP;41814;2.7;0;BE99
BE;1999-10-10;FDP;34280;2.2;0;BE99
BE;1999-10-10;GRAUE;17559;1.1;0;BE99
BE;1999-10-10;Tierschutzpartei;16732;1.1;0;BE99
BE;1999-10-10;NPD;13038;0.8;0;BE01
BE;1999-10-10;Sonstige;20920;1.3;0;BE99
BE;2001-10-21;SPD;481772;29.7;44;BE01
BE;2001-10-21;CDU;385692;23.8;35;BE01
BE;2001-10-21;PDS;366292;22.6;33;BE01
BE;2001-10-21;FDP;160953;9.9;15;BE01
BE;2001-10-21;GRÜNE;148066;9.1;14;BE01
BE;2001-10-21;GRAUE;22093;1.4;0;BE01
BE;2001-10-21;REP;21836;1.3;0;BE01
BE;2001-10-21;NPD;15110;0.9;0;BE01
BE;2001-10-21;STATT Partei;13396;0.8;0;BE01
BE;2001-10-21;Sonstige;8128;0.5;0;BE01
BE;2006-09-17;SPD;424054;30.8;53;BE06
BE;2006-09-17;CDU;294026;21.3;37;BE06
BE;2006-09-17;Die Linke.PDS;185185;13.4;23;BE06
BE;2006-09-17;GRÜNE;180865;13.1;23;BE06
BE;2006-09-17;FDP;104584;7.6;13;BE06
BE;2006-09-17;GRAUE;52884;3.8;0;BE06
BE;2006-09-17;WASG;40504;2.9;0;BE06
BE;2006-09-17;NPD;35229;2.6;0;BE06
BE;2006-09-17;REP;11922;0.9;0;BE06
BE;2006-09-17;Tierschutzpartei;11707;0.8;0;BE06
BE;2006-09-17;Eltern;10066;0.7;0;BE06
BE;2006-09-17;Sonstige;26329;1.9;0;BE06
BE;2011-09-18;SPD;413332;28.3;47;BE11
BE;2011-09-18;CDU;341158;23.3;39;BE11
BE;2011-09-18;GRÜNE;257063;17.6;29;BE11
BE;2011-09-18;DIE LINKE;171050;11.7;19;BE11
BE;2011-09-18;PIRATEN;130105;8.9;15;BE11
BE;2011-09-18;NPD;31241;2.1;0;BE11
BE;2011-09-18;FDP;26943;1.8;0;BE11
BE;2011-09-18;Tierschutzpartei;21654;1.5;0;BE11
BE;2011-09-18;pro Deutschland;17838;1.2;0;BE11
BE;2011-09-18;DIE FREIHEIT;14073;1.0;0;BE11
BE;2011-09-18;Die PARTEI;12861;0.9;0;BE11
BE;2011-09-18;BIG;8012;0.5;0;BE11
BE;2011-09-18;Sonstige;15855;1.1;0;BE11
BE;2016-09-18;SPD;352430;21.6;38;BE16
BE;2016-09-18;CDU;287997;17.6;31;BE16
BE;2016-09-18;DIE LINKE;255701;15.6;27;BE16
BE;2016-09-18;GRÜNE;248324;15.2;27;BE16
BE;2016-09-18;AfD;231492;14.2;25;BE16
BE;2016-09-18;FDP;109500;6.7;12;BE16
BE;2016-09-18;Die PARTEI;31924;2.0;0;BE16
BE;2016-09-18;Tierschutzpartei;30620;1.9;0;BE16
BE;2016-09-18;PIRATEN;28332;1.7;0;BE16
BE;2016-09-18;Graue Panther;18159;1.1;0;BE16
BE;2016-09-18;NPD;9459;0.6;0;BE16
BE;2016-09-18;Sonstige;31231;1.9;0;BE16
BE;2021-09-26;SPD;390329;21.4;36;BE21
BE;2021-09-26;GRÜNE;343871;18.9;32;BE21
BE;2021-09-26;CDU;328587;18.0;30;BE21
BE;2021-09-26;DIE LINKE;256063;14.1;24;BE21
BE;2021-09-26;AfD;145712;8.0;13;BE21
BE;2021-09-26;FDP;130201;7.1;12;BE21
BE;2021-09-26;Tierschutzpartei;40128;2.2;0;BE21
BE;2021-09-26;Die PARTEI;32800;1.8;0;BE21
BE;2021-09-26;dieBasis;23055;1.3;0;BE21
BE;2021-09-26;Volt;20205;1.1;0;BE21
BE;2021-09-26;Team Todenhöfer;18853;1.0;0;BE21
BE;2021-09-26;FREIE WÄHLER;15297;0.8;0;BE21
BE;2021-09-26;Die Grauen;12654;0.7;0;BE21
BE;2021-09-26;Sonstige;63909;3.5;0;BE21
BE;2023-02-12;CDU;428228;28.2;52;BE23
BE;2023-02-12;SPD;279017;18.4;34;BE23
BE;2023-02-12;GRÜNE;278964;18.4;34;BE23
BE;2023-02-12;DIE LINKE;185119;12.2;22;BE23
BE;2023-02-12;AfD;137871;9.1;17;BE23
BE;2023-02-12;FDP;70416;4.6;0;BE23
BE;2023-02-12;Tierschutzpartei;36273;2.4;0;BE23
BE;2023-02-12;Die PARTEI;21570;1.4;0;BE23
BE;2023-02-12;Volt;14047;0.9;0;BE23
BE;2023-02-12;dieBasis;8342;0.5;0;BE23
BE;2023-02-12;Sonstige;57013;3.8;0;BE23
BE;2026-09-20;DIE LINKE;468391;25.7;45;BE26
BE;2026-09-20;CDU;342746;18.8;33;BE26
BE;2026-09-20;AfD;296718;16.3;29;BE26
BE;2026-09-20;GRÜNE;260896;14.3;25;BE26
BE;2026-09-20;SPD;221116;12.1;21;BE26
BE;2026-09-20;BSW;86350;4.7;0;BE26
BE;2026-09-20;FDP;46384;2.5;0;BE26
BE;2026-09-20;Tierschutzpartei;38678;2.1;0;BE26
BE;2026-09-20;Volt;37950;2.1;0;BE26
BE;2026-09-20;Die PARTEI;13349;0.7;0;BE26
BE;2026-09-20;Sonstige;13094;0.7;0;BE26
BB;1990-10-14;SPD;487134;38.2;36;BB90
BB;1990-10-14;CDU;374572;29.4;27;BB90
BB;1990-10-14;PDS (LL/PDS);170804;13.4;13;BB90
BB;1990-10-14;FDP;84501;6.6;6;BB90
BB;1990-10-14;Bündnis 90;81725;6.4;6;BB90
BB;1990-10-14;Grüne;36238;2.8;0;BB90
BB;1990-10-14;REP;14631;1.1;0;BB90
BB;1990-10-14;Sonstige;24301;1.9;0;BB90
BB;1994-09-11;SPD;580422;54.1;52;BB94
BB;1994-09-11;CDU;200700;18.7;18;BB94
BB;1994-09-11;PDS;200628;18.7;18;BB94
BB;1994-09-11;GRÜNE/B 90;31033;2.9;0;BB94
BB;1994-09-11;FDP;23541;2.2;0;BB94
BB;1994-09-11;Bürger;10405;1.0;0;BB94
BB;1994-09-11;Sonstige (incl. REP);25290;2.4;0;BB94
BB;1999-09-05;SPD;433521;39.3;37;BB94
BB;1999-09-05;CDU;292634;26.5;25;BB94
BB;1999-09-05;PDS;257309;23.3;22;BB94
BB;1999-09-05;DVU;58247;5.3;5;BB94
BB;1999-09-05;GRÜNE/B 90;21410;1.9;0;BB94
BB;1999-09-05;FDP;20472;1.9;0;BB94
BB;1999-09-05;NPD;8137;0.7;0;BB94
BB;1999-09-05;BFWG;7008;0.6;0;BB94
BB;1999-09-05;Sonstige;3622;0.3;0;BB94
BB;2004-09-19;SPD;372942;31.9;33;BB04
BB;2004-09-19;PDS;326801;28.0;29;BB04
BB;2004-09-19;CDU;227062;19.4;20;BB04
BB;2004-09-19;DVU;71041;6.1;6;BB04
BB;2004-09-19;GRÜNE/B 90;42091;3.6;0;BB04
BB;2004-09-19;FDP;38890;3.3;0;BB04
BB;2004-09-19;FAMILIE;30843;2.6;0;BB04
BB;2004-09-19;50Plus;11875;1.0;0;BB04
BB;2004-09-19;AfW;11006;0.9;0;BB04
BB;2004-09-19;GRAUE;10470;0.9;0;BB04
BB;2004-09-19;AUB-Brandenburg;9993;0.9;0;BB04
BB;2004-09-19;BRB;5990;0.5;0;BB04
BB;2004-09-19;Sonstige;9905;0.8;0;BB04
BB;2009-09-27;SPD;458840;33.0;31;BB09
BB;2009-09-27;DIE LINKE;377112;27.2;26;BB09
BB;2009-09-27;CDU;274825;19.8;19;BB09
BB;2009-09-27;FDP;100123;7.2;7;BB09
BB;2009-09-27;GRÜNE/B 90;78550;5.7;5;BB09
BB;2009-09-27;NPD;35544;2.6;0;BB09
BB;2009-09-27;FREIE WÄHLER;23296;1.7;0;BB09
BB;2009-09-27;DVU;15903;1.1;0;BB09
BB;2009-09-27;50Plus;7905;0.6;0;BB09
BB;2009-09-27;RRP;6896;0.5;0;BB09
BB;2009-09-27;Sonstige;9728;0.7;0;BB09
BB;2014-09-14;SPD;315202;31.9;30;BB14
BB;2014-09-14;CDU;226835;23.0;21;BB14
BB;2014-09-14;DIE LINKE;183178;18.6;17;BB14
BB;2014-09-14;AfD;120077;12.2;11;BB14
BB;2014-09-14;GRÜNE/B 90;60767;6.2;6;BB14
BB;2014-09-14;BVB / FREIE WÄHLER;26317;2.7;3;BB14
BB;2014-09-14;NPD;21605;2.2;0;BB14
BB;2014-09-14;PIRATEN;14595;1.5;0;BB14
BB;2014-09-14;FDP;14376;1.5;0;BB14
BB;2014-09-14;Sonstige;4369;0.4;0;BB14
BB;2019-09-01;SPD;331238;26.2;25;BB19
BB;2019-09-01;AfD;297484;23.5;23;BB19
BB;2019-09-01;CDU;196988;15.6;15;BB19
BB;2019-09-01;GRÜNE/B 90;136364;10.8;10;BB19
BB;2019-09-01;DIE LINKE;135558;10.7;10;BB19
BB;2019-09-01;BVB / FREIE WÄHLER;63851;5.0;5;BB19
BB;2019-09-01;FDP;51660;4.1;0;BB19
BB;2019-09-01;Tierschutzpartei;32959;2.6;0;BB19
BB;2019-09-01;PIRATEN;8712;0.7;0;BB19
BB;2019-09-01;ÖDP;7237;0.6;0;BB19
BB;2019-09-01;Sonstige;3055;0.2;0;BB19
BB;2024-09-22;SPD;463800;30.9;32;BB24
BB;2024-09-22;AfD;438904;29.2;30;BB24
BB;2024-09-22;BSW;202421;13.5;14;BB24
BB;2024-09-22;CDU;181716;12.1;12;BB24
BB;2024-09-22;GRÜNE/B 90;62057;4.1;0;BB24
BB;2024-09-22;DIE LINKE;44706;3.0;0;BB24
BB;2024-09-22;BVB / FREIE WÄHLER;38573;2.6;0;BB24
BB;2024-09-22;Tierschutzpartei;30041;2.0;0;BB24
BB;2024-09-22;Plus;13584;0.9;0;BB24
BB;2024-09-22;FDP;12475;0.8;0;BB24
BB;2024-09-22;Sonstige;13342;0.9;0;BB24
BW;1980-03-16;CDU;2407798;53.4;68;BW
BW;1980-03-16;SPD;1468873;32.5;40;BW
BW;1980-03-16;FDP/DVP;374633;8.3;10;BW
BW;1980-03-16;GRÜNE;241303;5.3;6;BW
BW;1980-03-16;Sonstige;20402;0.5;0;BW
BW;1984-03-25;CDU;2412085;51.9;68;BW
BW;1984-03-25;SPD;1507088;32.4;41;BW
BW;1984-03-25;GRÜNE;372374;8.0;9;BW
BW;1984-03-25;FDP/DVP;333386;7.2;8;BW
BW;1984-03-25;Sonstige;25253;0.5;0;BW
BW;1988-03-20;CDU;2392626;49.0;66;BW
BW;1988-03-20;SPD;1562678;32.0;42;BW
BW;1988-03-20;GRÜNE;383099;7.9;10;BW
BW;1988-03-20;FDP/DVP;285932;5.9;7;BW
BW;1988-03-20;NPD;101889;2.1;0;BW
BW;1988-03-20;ÖDP;69823;1.4;0;BW
BW;1988-03-20;REP;46904;1.0;0;BW
BW;1988-03-20;Sonstige;35111;0.7;0;BW
BW;1992-04-05;CDU;1960016;39.6;64;BW
BW;1992-04-05;SPD;1454477;29.4;46;BW
BW;1992-04-05;REP;539014;10.9;15;BW
BW;1992-04-05;GRÜNE;467781;9.5;13;BW
BW;1992-04-05;FDP/DVP;291199;5.9;8;BW
BW;1992-04-05;ÖDP;93604;1.9;0;BW
BW;1992-04-05;NPD;44416;0.9;0;BW
BW;1992-04-05;DIE GRAUEN;28719;0.6;0;BW
BW;1992-04-05;PBC;27272;0.6;0;BW
BW;1992-04-05;DLVH;23255;0.5;0;BW
BW;1992-04-05;Sonstige;19446;0.4;0;BW
BW;1996-03-24;CDU;1974619;41.3;69;BW
BW;1996-03-24;SPD;1199123;25.1;39;BW
BW;1996-03-24;GRÜNE;580801;12.1;19;BW
BW;1996-03-24;FDP/DVP;458478;9.6;14;BW
BW;1996-03-24;REP;437228;9.1;14;BW
BW;1996-03-24;ÖDP;69775;1.5;0;BW
BW;1996-03-24;PBC;23250;0.5;0;BW
BW;1996-03-24;Sonstige;40855;0.9;0;BW
BW;2001-03-25;CDU;2029806;44.8;63;BW
BW;2001-03-25;SPD;1508358;33.3;45;BW
BW;2001-03-25;FDP/DVP;367580;8.1;10;BW
BW;2001-03-25;GRÜNE;350383;7.7;10;BW
BW;2001-03-25;REP;198534;4.4;0;BW
BW;2001-03-25;ÖDP;32451;0.7;0;BW
BW;2001-03-25;PBC;20528;0.5;0;BW
BW;2001-03-25;Sonstige;23123;0.5;0;BW
BW;2006-03-26;CDU;1748766;44.2;69;BW
BW;2006-03-26;SPD;996207;25.2;38;BW
BW;2006-03-26;GRÜNE;462889;11.7;17;BW
BW;2006-03-26;FDP/DVP;421994;10.7;15;BW
BW;2006-03-26;WASG;121753;3.1;0;BW
BW;2006-03-26;REP;100081;2.5;0;BW
BW;2006-03-26;NPD;29219;0.7;0;BW
BW;2006-03-26;PBC;26759;0.7;0;BW
BW;2006-03-26;ÖDP;21761;0.5;0;BW
BW;2006-03-26;Sonstige;31186;0.8;0;BW
BW;2011-03-27;CDU;1943912;39.0;60;BW
BW;2011-03-27;GRÜNE;1206182;24.2;36;BW
BW;2011-03-27;SPD;1152594;23.1;35;BW
BW;2011-03-27;FDP/DVP;262784;5.3;7;BW
BW;2011-03-27;DIE LINKE;139700;2.8;0;BW
BW;2011-03-27;PIRATEN;103618;2.1;0;BW
BW;2011-03-27;REP;56723;1.1;0;BW
BW;2011-03-27;NPD;48227;1.0;0;BW
BW;2011-03-27;ÖDP;42539;0.9;0;BW
BW;2011-03-27;Sonstige;27440;0.6;0;BW
BW;2016-03-13;GRÜNE;1623107;30.3;47;BW
BW;2016-03-13;CDU;1447462;27.0;42;BW
BW;2016-03-13;AfD;809564;15.1;23;BW
BW;2016-03-13;SPD;679727;12.7;19;BW
BW;2016-03-13;FDP/DVP;445498;8.3;12;BW
BW;2016-03-13;DIE LINKE;156240;2.9;0;BW
BW;2016-03-13;ALFA;54713;1.0;0;BW
BW;2016-03-13;ÖDP;38517;0.7;0;BW
BW;2016-03-13;Sonstige;106422;2.0;0;BW
BW;2021-03-14;GRÜNE;1586192;32.6;58;BW
BW;2021-03-14;CDU;1168975;24.1;42;BW
BW;2021-03-14;SPD;535489;11.0;19;BW
BW;2021-03-14;FDP/DVP;508429;10.5;18;BW
BW;2021-03-14;AfD;473485;9.7;17;BW
BW;2021-03-14;DIE LINKE;173317;3.6;0;BW
BW;2021-03-14;FREIE WÄHLER;146259;3.0;0;BW
BW;2021-03-14;Die PARTEI;59463;1.2;0;BW
BW;2021-03-14;dieBasis;48497;1.0;0;BW
BW;2021-03-14;KlimalisteBW;42685;0.9;0;BW
BW;2021-03-14;W2020;41128;0.8;0;BW
BW;2021-03-14;ÖDP;37819;0.8;0;BW
BW;2021-03-14;Volt;22782;0.5;0;BW
BW;2021-03-14;Sonstige;15131;0.3;0;BW
BW;2026-03-08;GRÜNE;1623208;30.2;56;BW26
BW;2026-03-08;CDU;1595929;29.7;56;BW26
BW;2026-03-08;AfD;1010574;18.8;35;BW26
BW;2026-03-08;SPD;298297;5.5;10;BW26
BW;2026-03-08;DIE LINKE;236975;4.4;0;BW26
BW;2026-03-08;FDP/DVP;235598;4.4;0;BW26
BW;2026-03-08;FREIE WÄHLER;102716;1.9;0;BW26
BW;2026-03-08;BSW;76439;1.4;0;BW26
BW;2026-03-08;Tierschutzpartei;49827;0.9;0;BW26
BW;2026-03-08;Volt;45842;0.9;0;BW26
BW;2026-03-08;Sonstige;99704;1.9;0;BW26
"""

# Harmonised party codes (for change computation and role coding)
HARMONISE = {
 "CDU":"CDU","SPD":"SPD","FDP":"FDP","FDP/DVP":"FDP",
 "AL":"GRUENE","GRÜNE/AL":"GRUENE","Bündnis 90/Grüne/UFV":"GRUENE","GRÜNE":"GRUENE","GRÜNE/B 90":"GRUENE",
 "Bündnis 90":"GRUENE","Grüne":"GRUENE",
 "PDS":"LINKE","PDS (LL/PDS)":"LINKE","Die Linke.PDS":"LINKE","DIE LINKE":"LINKE",
 "AfD":"AFD","REP":"REP","NPD":"NPD","DVU":"DVU","PIRATEN":"PIRATEN","BSW":"BSW",
 "FREIE WÄHLER":"FW","BVB / FREIE WÄHLER":"FW",
 "GRAUE":"GRAUE","Graue Panther":"GRAUE","Die Grauen":"GRAUE","DIE GRAUEN":"GRAUE",
 "Tierschutzpartei":"TIERSCHUTZ","Die PARTEI":"PARTEI","ÖDP":"OEDP","PBC":"PBC","Volt":"VOLT",
 "dieBasis":"BASIS","SEW":"SEW","WASG":"WASG","50Plus":"50PLUS",
 "Sonstige":"OTHER","Sonstige (incl. REP)":"OTHER",
}
PARTY_FAMILY = {
 "CDU":"Christian democratic / conservative","SPD":"Social democratic","FDP":"Liberal",
 "GRUENE":"Green","LINKE":"Left / post-socialist","AFD":"Radical right","REP":"Radical right",
 "NPD":"Radical right","DVU":"Radical right","PIRATEN":"Pirate / digital","BSW":"Left-conservative / populist",
 "FW":"Free voters / regionalist","SEW":"Communist","WASG":"Left",
}

# ---------------- Government timeline (composition spells) ----------------
# state;start;end;cabinet;head;head_party;gov_parties(+ sep);tolerating;caretaker_note;date_precision;src;note
# end = start of next row (exclusive) — leave last row open (NA)
GOV = """
BE;1981-01-23;1981-06-11;Senat Vogel;Hans-Jochen Vogel;SPD;SPD+FDP;;;day;https://en.wikipedia.org/wiki/List_of_mayors_of_Berlin;Caretaker from 1981-05-10 election until Weizsäcker election
BE;1981-06-11;1983-03-17;Senat Weizsäcker (minority);Richard von Weizsäcker;CDU;CDU;FDP (several MdA);;day;https://www.berlin.de/rbmskzl/politik/senat/buergermeistergalerie/artikel.4633.php;CDU minority Senate tolerated by part of FDP group
BE;1983-03-17;1984-02-09;Senat Weizsäcker (CDU-FDP);Richard von Weizsäcker;CDU;CDU+FDP;;;day;https://www.bpb.de;FDP senators from 1983-03-17
BE;1984-02-09;1985-04-18;Senat Diepgen I;Eberhard Diepgen;CDU;CDU+FDP;;;day;https://www.kas.de/web/geschichte-der-cdu/personen/biogramm-detail/-/content/eberhard-diepgen;
BE;1985-04-18;1989-03-16;Senat Diepgen II;Eberhard Diepgen;CDU;CDU+FDP;;;day;https://www.archivportal-d.de/item/P65TF4GXQJLDLKBJA6GCGYKI2ZHMRCLE;start = date of archived photo of the newly elected Senate
BE;1989-03-16;1990-11-19;Senat Momper (SPD-AL);Walter Momper;SPD;SPD+AL;;;day;https://de.wikipedia.org/wiki/Senat_Momper;AL left coalition 1990-11-15, AL senators resigned 1990-11-19; from 1990-10-03 jointly with East Berlin Magistrat Schwierzina
BE;1990-11-19;1991-01-24;Senat Momper (SPD minority);Walter Momper;SPD;SPD;;;day;https://de.wikipedia.org/wiki/Senat_Momper;SPD-only rump Senate; caretaker after 1990-12-02 election
BE;1991-01-24;1996-01-25;Senat Diepgen III;Eberhard Diepgen;CDU;CDU+SPD;;;day (start), approx (end);https://www.kas.de/web/geschichte-der-cdu/personen/biogramm-detail/-/content/eberhard-diepgen;Grand coalition
BE;1996-01-25;1999-12-09;Senat Diepgen IV;Eberhard Diepgen;CDU;CDU+SPD;;;approx (start and end unverified);https://de.wikipedia.org/wiki/Senat_Diepgen_IV;Start date = Diepgen re-election, not verified in fetched sources (sources only say 'early 1996'); coalition composition unaffected
BE;1999-12-09;2001-06-16;Senat Diepgen V;Eberhard Diepgen;CDU;CDU+SPD;;;approx (start), day (end);https://www.bpb.de/themen/zeit-kulturgeschichte/deutschland-chronik/132662/7-dezember-1999/;Start = Senate election date as scheduled per bpb chronicle; ended by vote removing Diepgen (SPD, PDS, Grüne)
BE;2001-06-16;2002-01-17;Senat Wowereit I;Klaus Wowereit;SPD;SPD+GRÜNE;PDS;;day;https://de.wikipedia.org/wiki/Senat_Wowereit_I;Minority Senate tolerated by PDS after grand coalition collapsed (Bankenskandal)
BE;2002-01-17;2006-11-23;Senat Wowereit II;Klaus Wowereit;SPD;SPD+PDS;;;day;https://de.wikipedia.org/wiki/Senat_Wowereit_II;
BE;2006-11-23;2011-11-24;Senat Wowereit III;Klaus Wowereit;SPD;SPD+LINKE;;;day;https://de.wikipedia.org/wiki/Senat_Wowereit_III;Die Linke.PDS / DIE LINKE
BE;2011-11-24;2014-12-11;Senat Wowereit IV;Klaus Wowereit;SPD;SPD+CDU;;;day;https://de.wikipedia.org/wiki/Senat_Wowereit_IV;
BE;2014-12-11;2016-12-08;Senat Müller I;Michael Müller;SPD;SPD+CDU;;;day;https://de.wikipedia.org/wiki/Senat_Müller_I;Head change without election
BE;2016-12-08;2021-12-21;Senat Müller II;Michael Müller;SPD;SPD+LINKE+GRÜNE;;;day;https://de.wikipedia.org/wiki/Senat_Müller_II;
BE;2021-12-21;2023-04-27;Senat Giffey;Franziska Giffey;SPD;SPD+GRÜNE+LINKE;;;day;https://de.wikipedia.org/wiki/Senat_Giffey;
BE;2023-04-27;NA;Senat Wegner;Kai Wegner;CDU;CDU+SPD;;;day;https://de.wikipedia.org/wiki/Senat_Wegner;Caretaker since 2026-09-20 election (no new Senate found as of 2026-10-13)
BB;1990-10-14;1990-11-01;No state government yet (Land re-established 1990-10-03);NA;;NONE;;caretaker;day;https://de.wikipedia.org/wiki/Kabinett_Stolpe_I;Pre-formation period: Landtag elected, first cabinet not yet formed
BB;1990-11-01;1994-03-01;Kabinett Stolpe I (Ampel);Manfred Stolpe;SPD;SPD+FDP+Bündnis 90;;;month (end);https://de.wikipedia.org/wiki/Kabinett_Stolpe_I;Bündnis 90 group left coalition in March 1994 (exact day not verified); end coded as first of month
BB;1994-03-01;1994-10-11;Kabinett Stolpe I (SPD-FDP minority);Manfred Stolpe;SPD;SPD+FDP;;;month (start);https://de.wikipedia.org/wiki/Kabinett_Stolpe_I;Bündnis 90 ministers (Platzeck, Resch) stayed in office as individuals
BB;1994-10-11;1999-10-13;Kabinett Stolpe II;Manfred Stolpe;SPD;SPD;;;day;https://de.wikipedia.org/wiki/Kabinett_Stolpe_II;SPD absolute majority
BB;1999-10-13;2002-06-26;Kabinett Stolpe III;Manfred Stolpe;SPD;SPD+CDU;;;day;https://de.wikipedia.org/wiki/Kabinett_Stolpe_III;
BB;2002-06-26;2004-10-13;Kabinett Platzeck I;Matthias Platzeck;SPD;SPD+CDU;;;day;https://de.wikipedia.org/wiki/Kabinett_Platzeck_I;Head change without election
BB;2004-10-13;2009-11-06;Kabinett Platzeck II;Matthias Platzeck;SPD;SPD+CDU;;;day;https://de.wikipedia.org/wiki/Kabinett_Platzeck_II;
BB;2009-11-06;2013-08-28;Kabinett Platzeck III;Matthias Platzeck;SPD;SPD+LINKE;;;day;https://de.wikipedia.org/wiki/Kabinett_Platzeck_III;
BB;2013-08-28;2014-11-05;Kabinett Woidke I;Dietmar Woidke;SPD;SPD+LINKE;;;day;https://de.wikipedia.org/wiki/Kabinett_Woidke_I;Head change without election
BB;2014-11-05;2019-11-20;Kabinett Woidke II;Dietmar Woidke;SPD;SPD+LINKE;;;day;https://de.wikipedia.org/wiki/Kabinett_Woidke_II;
BB;2019-11-20;2024-12-11;Kabinett Woidke III;Dietmar Woidke;SPD;SPD+CDU+GRÜNE;;;day;https://de.wikipedia.org/wiki/Kabinett_Woidke_III;Kenia coalition
BB;2024-12-11;2026-01-06;Kabinett Woidke IV (SPD-BSW);Dietmar Woidke;SPD;SPD+BSW;;;day;https://www.brandenburg.de/media_fast/365/260106%20PM%20Stk%20Woidke%20Koalition.pdf;Coalition ended 2026-01-06 after BSW group split
BB;2026-01-06;2026-03-18;Kabinett Woidke IV (SPD minority);Dietmar Woidke;SPD;SPD;;;day;https://www.nordkurier.de/politik/wie-geht-es-nach-dem-aus-fuer-rot-lila-in-brandenburg-weiter-4246357;Minority phase; (ex-)BSW ministers remained for a transition
BB;2026-03-18;NA;Kabinett Woidke (SPD-CDU);Dietmar Woidke;SPD;SPD+CDU;;;day;https://www.zdfheute.de/politik/deutschland/brandenburg-spd-cdu-koalition-minister-vereidigung-100.html;Ministers sworn in 2026-03-18; cabinet name not yet established
BW;1978-08-30;1980-06-03;Kabinett Späth I;Lothar Späth;CDU;CDU;;;day;https://www.kas.de/de/web/geschichte-der-cdu/personen/biogramm-detail/-/content/lothar-spaeth;Späth elected 1978-08-30
BW;1980-06-03;1984-06-05;Kabinett Späth II;Lothar Späth;CDU;CDU;;;approx (= constituent session, MP re-election day not verified);https://www.baden-wuerttemberg.de/de/regierung/ministerpraesident/ministerpraesidenten-seit-1952;CDU absolute majority
BW;1984-06-05;1988-06-07;Kabinett Späth III;Lothar Späth;CDU;CDU;;;approx (= constituent session, MP re-election day not verified);https://www.baden-wuerttemberg.de/de/regierung/ministerpraesident/ministerpraesidenten-seit-1952;CDU absolute majority
BW;1988-06-07;1991-01-13;Kabinett Späth IV;Lothar Späth;CDU;CDU;;;approx (start), day (end);https://de.wikipedia.org/wiki/Lothar_Späth;Späth resigned 1991-01-13 (Traumschiff affair)
BW;1991-01-13;1991-01-22;Interim (after Späth resignation);NA;CDU;CDU;;caretaker;day;https://de.wikipedia.org/wiki/Erwin_Teufel;Späth resigned 1991-01-13; Teufel elected 1991-01-22
BW;1991-01-22;1992-06-11;Kabinett Teufel I;Erwin Teufel;CDU;CDU;;;day;https://de.wikipedia.org/wiki/Erwin_Teufel;
BW;1992-06-11;1996-06-12;Kabinett Teufel II;Erwin Teufel;CDU;CDU+SPD;;;day;https://kas.de/documents/252038/253252/cv_teufel.pdf;Grand coalition
BW;1996-06-12;2001-06-13;Kabinett Teufel III;Erwin Teufel;CDU;CDU+FDP;;;day;https://kas.de/documents/252038/253252/cv_teufel.pdf;
BW;2001-06-13;2005-04-21;Kabinett Teufel IV;Erwin Teufel;CDU;CDU+FDP;;;day;https://de.wikipedia.org/wiki/Erwin_Teufel;Teufel resigned effective 2005-04-19, Oettinger elected 2005-04-21 (2-day acting interval absorbed here)
BW;2005-04-21;2006-06-14;Kabinett Oettinger I;Günther Oettinger;CDU;CDU+FDP;;;day;https://de.wikipedia.org/wiki/Günther_Oettinger;Head change without election
BW;2006-06-14;2010-02-10;Kabinett Oettinger II;Günther Oettinger;CDU;CDU+FDP;;;day;https://de.wikipedia.org/wiki/Günther_Oettinger;
BW;2010-02-10;2011-05-12;Kabinett Mappus;Stefan Mappus;CDU;CDU+FDP;;;day;https://de.wikipedia.org/wiki/Stefan_Mappus;Head change without election
BW;2011-05-12;2016-05-12;Kabinett Kretschmann I;Winfried Kretschmann;GRÜNE;GRÜNE+SPD;;;day;https://de.wikipedia.org/wiki/Winfried_Kretschmann;First Green-led state government
BW;2016-05-12;2021-05-12;Kabinett Kretschmann II;Winfried Kretschmann;GRÜNE;GRÜNE+CDU;;;day;https://de.wikipedia.org/wiki/Winfried_Kretschmann;
BW;2021-05-12;2026-05-13;Kabinett Kretschmann III;Winfried Kretschmann;GRÜNE;GRÜNE+CDU;;;day;https://de.wikipedia.org/wiki/Winfried_Kretschmann;
BW;2026-05-13;NA;Kabinett Özdemir;Cem Özdemir;GRÜNE;GRÜNE+CDU;;;day;https://en.wikipedia.org/wiki/%C3%96zdemir_cabinet;
"""

# Individual cabinets (finer grain, informational)
# state;cabinet;head;head_party;coalition;start;end;note;src
CABINETS = """
BE;Senat Vogel;Hans-Jochen Vogel;SPD;SPD, FDP;1981-01-23;1981-06-11;;https://en.wikipedia.org/wiki/List_of_mayors_of_Berlin
BE;Senat Weizsäcker;Richard von Weizsäcker;CDU;CDU (minority), from 1983-03-17 CDU, FDP;1981-06-11;1984-02-09;tolerated by several FDP MdA until 1983;https://www.berlin.de/rbmskzl/politik/senat/buergermeistergalerie/artikel.4633.php
BE;Senat Diepgen I;Eberhard Diepgen;CDU;CDU, FDP;1984-02-09;1985-04-18;;https://www.kas.de/web/geschichte-der-cdu/personen/biogramm-detail/-/content/eberhard-diepgen
BE;Senat Diepgen II;Eberhard Diepgen;CDU;CDU, FDP;1985-04-18;1989-03-16;start = date of archived photo of newly elected Senate;https://www.archivportal-d.de/item/P65TF4GXQJLDLKBJA6GCGYKI2ZHMRCLE
BE;Senat Momper;Walter Momper;SPD;SPD, AL (AL left 1990-11-15/19);1989-03-16;1991-01-24;;https://de.wikipedia.org/wiki/Senat_Momper
BE;Magistrat Schwierzina (East Berlin);Tino Schwierzina;SPD;NA;1990-05-30;1991-01-24;East Berlin city government after 1990-05-06 election; not part of Abgeordnetenhaus system;https://de.wikipedia.org/wiki/Magistrat_Schwierzina
BE;Senat Diepgen III;Eberhard Diepgen;CDU;CDU, SPD;1991-01-24;NA (early 1996);;https://de.wikipedia.org/wiki/Senat_Diepgen_III
BE;Senat Diepgen IV;Eberhard Diepgen;CDU;CDU, SPD;NA (early 1996);NA (Dec 1999);;https://de.wikipedia.org/wiki/Senat_Diepgen_IV
BE;Senat Diepgen V;Eberhard Diepgen;CDU;CDU, SPD;NA (Dec 1999, bpb lists Senate election scheduled for 1999-12-09);2001-06-16;ended by constructive vote removing Diepgen;https://www.bpb.de/themen/zeit-kulturgeschichte/deutschland-chronik/132662/7-dezember-1999/
BE;Senat Wowereit I;Klaus Wowereit;SPD;SPD, GRÜNE (minority, tolerated by PDS);2001-06-16;2002-01-17;;https://de.wikipedia.org/wiki/Senat_Wowereit_I
BE;Senat Wowereit II;Klaus Wowereit;SPD;SPD, PDS;2002-01-17;2006-11-23;;https://de.wikipedia.org/wiki/Senat_Wowereit_II
BE;Senat Wowereit III;Klaus Wowereit;SPD;SPD, Die Linke.PDS / DIE LINKE;2006-11-23;2011-11-24;;https://de.wikipedia.org/wiki/Senat_Wowereit_III
BE;Senat Wowereit IV;Klaus Wowereit;SPD;SPD, CDU;2011-11-24;2014-12-11;;https://de.wikipedia.org/wiki/Senat_Wowereit_IV
BE;Senat Müller I;Michael Müller;SPD;SPD, CDU;2014-12-11;2016-12-08;;https://de.wikipedia.org/wiki/Senat_Müller_I
BE;Senat Müller II;Michael Müller;SPD;SPD, DIE LINKE, GRÜNE;2016-12-08;2021-12-21;;https://de.wikipedia.org/wiki/Senat_Müller_II
BE;Senat Giffey;Franziska Giffey;SPD;SPD, GRÜNE, DIE LINKE;2021-12-21;2023-04-27;;https://de.wikipedia.org/wiki/Senat_Giffey
BE;Senat Wegner;Kai Wegner;CDU;CDU, SPD;2023-04-27;NA (in office / caretaker after 2026-09-20);;https://de.wikipedia.org/wiki/Senat_Wegner
BB;Kabinett Stolpe I;Manfred Stolpe;SPD;SPD, FDP, Bündnis 90 (B90 left March 1994);1990-11-01;1994-10-11;;https://de.wikipedia.org/wiki/Kabinett_Stolpe_I
BB;Kabinett Stolpe II;Manfred Stolpe;SPD;SPD;1994-10-11;1999-10-13;;https://de.wikipedia.org/wiki/Kabinett_Stolpe_II
BB;Kabinett Stolpe III;Manfred Stolpe;SPD;SPD, CDU;1999-10-13;2002-06-26;;https://de.wikipedia.org/wiki/Kabinett_Stolpe_III
BB;Kabinett Platzeck I;Matthias Platzeck;SPD;SPD, CDU;2002-06-26;2004-10-13;;https://de.wikipedia.org/wiki/Kabinett_Platzeck_I
BB;Kabinett Platzeck II;Matthias Platzeck;SPD;SPD, CDU;2004-10-13;2009-11-06;;https://de.wikipedia.org/wiki/Kabinett_Platzeck_II
BB;Kabinett Platzeck III;Matthias Platzeck;SPD;SPD, DIE LINKE;2009-11-06;2013-08-28;;https://de.wikipedia.org/wiki/Kabinett_Platzeck_III
BB;Kabinett Woidke I;Dietmar Woidke;SPD;SPD, DIE LINKE;2013-08-28;2014-11-05;;https://de.wikipedia.org/wiki/Kabinett_Woidke_I
BB;Kabinett Woidke II;Dietmar Woidke;SPD;SPD, DIE LINKE;2014-11-05;2019-11-20;;https://de.wikipedia.org/wiki/Kabinett_Woidke_II
BB;Kabinett Woidke III;Dietmar Woidke;SPD;SPD, CDU, GRÜNE;2019-11-20;2024-12-11;;https://de.wikipedia.org/wiki/Kabinett_Woidke_III
BB;Kabinett Woidke IV;Dietmar Woidke;SPD;SPD, BSW (coalition ended 2026-01-06; then SPD minority);2024-12-11;2026-03-18;;https://de.wikipedia.org/wiki/Kabinett_Woidke_IV
BB;Kabinett Woidke (SPD-CDU, 2026);Dietmar Woidke;SPD;SPD, CDU;2026-03-18;NA (in office);name not established in sources found;https://www.zdfheute.de/politik/deutschland/brandenburg-spd-cdu-koalition-minister-vereidigung-100.html
BW;Kabinett Späth II;Lothar Späth;CDU;CDU;NA (1980);NA (1984);re-election dates not found;https://www.baden-wuerttemberg.de/de/regierung/ministerpraesident/ministerpraesidenten-seit-1952
BW;Kabinett Späth III;Lothar Späth;CDU;CDU;NA (1984);NA (1988);re-election dates not found;https://www.baden-wuerttemberg.de/de/regierung/ministerpraesident/ministerpraesidenten-seit-1952
BW;Kabinett Späth IV;Lothar Späth;CDU;CDU;NA (1988);1991-01-13;Späth resigned (Traumschiff affair);https://de.wikipedia.org/wiki/Lothar_Späth
BW;Kabinett Teufel I;Erwin Teufel;CDU;CDU;1991-01-22;1992-06-11;;https://de.wikipedia.org/wiki/Erwin_Teufel
BW;Kabinett Teufel II;Erwin Teufel;CDU;CDU, SPD;1992-06-11;1996-06-12;;https://kas.de/documents/252038/253252/cv_teufel.pdf
BW;Kabinett Teufel III;Erwin Teufel;CDU;CDU, FDP/DVP;1996-06-12;2001-06-13;;https://kas.de/documents/252038/253252/cv_teufel.pdf
BW;Kabinett Teufel IV;Erwin Teufel;CDU;CDU, FDP/DVP;2001-06-13;2005-04-19;resigned effective 2005-04-19;https://de.wikipedia.org/wiki/Erwin_Teufel
BW;Kabinett Oettinger I;Günther Oettinger;CDU;CDU, FDP/DVP;2005-04-21;2006-06-14;;https://de.wikipedia.org/wiki/Günther_Oettinger
BW;Kabinett Oettinger II;Günther Oettinger;CDU;CDU, FDP/DVP;2006-06-14;2010-02-10;left for EU Commission;https://de.wikipedia.org/wiki/Günther_Oettinger
BW;Kabinett Mappus;Stefan Mappus;CDU;CDU, FDP/DVP;2010-02-10;2011-05-12;;https://de.wikipedia.org/wiki/Stefan_Mappus
BW;Kabinett Kretschmann I;Winfried Kretschmann;GRÜNE;GRÜNE, SPD;2011-05-12;2016-05-12;;https://de.wikipedia.org/wiki/Winfried_Kretschmann
BW;Kabinett Kretschmann II;Winfried Kretschmann;GRÜNE;GRÜNE, CDU;2016-05-12;2021-05-12;;https://de.wikipedia.org/wiki/Winfried_Kretschmann
BW;Kabinett Kretschmann III;Winfried Kretschmann;GRÜNE;GRÜNE, CDU;2021-05-12;2026-05-13;;https://de.wikipedia.org/wiki/Winfried_Kretschmann
BW;Kabinett Özdemir;Cem Özdemir;GRÜNE;GRÜNE, CDU;2026-05-13;NA (in office);;https://en.wikipedia.org/wiki/%C3%96zdemir_cabinet
"""

# Legislative terms (Wahlperioden)
# state;wahlperiode;constituent_session;term_end;precision_note;src
TERMS = """
BE;9;NA;NA;constituent session date not found;
BE;10;NA;NA;constituent session date not found;
BE;11;NA;1991-01-11;;https://de.wikipedia.org/wiki/Abgeordnetenhaus_von_Berlin
BE;12;1991-01-11;NA;constituent session in Nikolaikirche;https://de.wikipedia.org/wiki/Abgeordnetenhaus_von_Berlin
BE;13;NA;NA;constituent session date not found;
BE;14;NA;2001-11-29;end inferred from end of Diepgen's mandate (29 Nov 2001) – verify;https://en.wikipedia.org/wiki/Eberhard_Diepgen
BE;15;2001-11-29;2006-10-26;start inferred (see WP14) – verify;https://www.parlament-berlin.de/ados/16/IIIPlen/protokoll/plen16-001-bp.pdf
BE;16;2006-10-26;2011-10-27;;https://www.parlament-berlin.de/ados/16/IIIPlen/protokoll/plen16-001-bp.pdf
BE;17;2011-10-27;2016-10-27;;https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Abgeordnetenhauses_von_Berlin_(17._Wahlperiode)
BE;18;2016-10-27;2021-11-04;;https://www.parlament-berlin.de/ados/18/IIIPlen/protokoll/plen18-001-pp.pdf
BE;19;2021-11-04;NA;re-constituted 2023-03-16 after the repeat election of 2023-02-12;https://www.parlament-berlin.de/ados/19/IIIPlen/protokoll/plen19-001-pp.pdf
BE;20;NA;NA;constituent session pending/not found (election 2026-09-20);
BB;1;1990-10-26;1994-10-11;;https://de.wikipedia.org/wiki/Landtagswahl_in_Brandenburg_1990
BB;2;1994-10-11;1999-09-29;;https://de.wikipedia.org/wiki/Landtagswahl_in_Brandenburg_1994
BB;3;1999-09-29;2004-10-13;;https://de.wikipedia.org/wiki/Landtagswahl_in_Brandenburg_1999
BB;4;2004-10-13;2009-10-21;;https://www.landtag.brandenburg.de/media_fast/6/Handbuch-web.pdf
BB;5;2009-10-21;2014-10-08;;https://www.landtag.brandenburg.de/media_fast/6/Landtag%20HB_web.pdf
BB;6;2014-10-08;2019-09-25;;https://www.landtag.brandenburg.de/media_fast/6/Statistik_6_WP_25-09-2019pdf.pdf
BB;7;2019-09-25;2024-10-17;;https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_Brandenburg_(7._Wahlperiode)
BB;8;2024-10-17;NA;ongoing;https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_Brandenburg_(8._Wahlperiode)
BW;8;1980-06-03;1984-06-05;official term 1980-06-01 to 1984-05-31 (derived from Art. 30 LV);https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_von_Baden-Württemberg_(8._Wahlperiode)
BW;9;1984-06-05;1988-06-07;official term 1984-06-01 to 1988-05-31 (derived);https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_von_Baden-Württemberg_(9._Wahlperiode)
BW;10;1988-06-07;1992-06-10;official term 1988-06-01 to 1992-05-31 (derived);https://www.landtag-bw.de/files/live/sites/LTBW/files/dokumente/drucksachen/WP10_Sprechregister.pdf
BW;11;1992-06-10;1996-06-11;official term 1992-06-01 to 1996-05-31 (derived);https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_von_Baden-Württemberg_(11._Wahlperiode)
BW;12;1996-06-11;2001-06-12;official term 1996-06-01 to 2001-05-31 (derived; 5-year terms from 1996);https://www.landtag-bw.de/files/live/sites/LTBW/files/dokumente/drucksachen/WP12_Sprechregister.pdf
BW;13;2001-06-12;2006-06-13;official term 2001-06-01 to 2006-05-31 (derived);https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_von_Baden-Württemberg_(13._Wahlperiode)
BW;14;2006-06-13;2011-05-11;official term 2006-06-01 to 2011-04-30 (Drs. 14/2490);https://www.landtag-bw.de/resource/blob/72070/55a620408c7b7fcf008db111323e914a/14_2490_D.pdf
BW;15;2011-05-11;2016-05-11;official term 2011-05-01 to 2016-04-30;https://www.landtag-bw.de/WP15/Plp/15_0001_11052011.pdf
BW;16;2016-05-11;2021-05-11;official term 2016-05-01 to 2021-04-30;https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Landtags_von_Baden-Württemberg_(16._Wahlperiode)
BW;17;2021-05-11;2026-05-12;official term 2021-05-01 to 2026-04-30;https://de.wikipedia.org/wiki/Landtag_von_Baden-Württemberg
BW;18;2026-05-12;NA;ongoing;https://www.landtag-bw.de/resource/blob/634112/3082ae7deb22ab0ee394e778d615e586/2026-05-12_01_Plenarsitzung.pdf
"""
