import text
nan=""
section_words = {'start': -1, '1': 279, 'end': -2}
the_text =  [('ΑΓΑΘΟΣ', 0, 'αγαθος', '', '', '1', 1), ('ΑΓΑΠΗ', 1, 'αγαπη', '', '', '1', 1), ('ΑΓΓΕΛΛΩ', 2, 'αγγελλω', '', '', '1', 1), ('ΑΓΩ', 3, 'αγω', '', '', '1', 1), ('ΑΔΕΛΦΟΣ', 4, 'αδελφος', '', '', '1', 1), ('ΑΙΜΑ', 5, 'αιμα', '', '', '1', 1), ('ΑΙΡΕΩ', 6, 'αιρεω', '', '', '1', 1), ('ΑΙΤΕΩ', 7, 'αιτεω', '', '', '1', 1), ('ΑΙΤΙΑ', 8, 'αιτια', '', '', '1', 1), ('ΑΚΟΥΩ', 9, 'ακουω', '', '', '1', 1), ('ΑΛΗΘΕΙΑ', 10, 'αληθεια', '', '', '1', 1), ('ΑΛΗΘΗΣ', 11, 'αληθης', '', '', '1', 1), ('ΑΛΛΑ', 12, 'αλλα', '', '', '1', 1), ('ΑΛΛΟΣ', 13, 'αλλος', '', '', '1', 1), ('ΑΜΑΡΤΑΝΩ', 14, 'αμαρτανω', '', '', '1', 1), ('ΑΜΕΙΝΩΝ', 15, 'αμεινων', '', '', '1', 1), ('ΑΝΑ', 16, 'ανα', '', '', '1', 1), ('ΑΝΑΓΚΗ', 17, 'αναγκη', '', '', '1', 1), ('ΑΝΗΡ', 18, 'ανηρ', '', '', '1', 1), ('ΑΝΘΡΩΠΟΣ', 19, 'ανθρωπος', '', '', '1', 1), ('ΑΞΙΟΣ', 20, 'αξιος', '', '', '1', 1), ('ΑΠΟ', 21, 'απο', '', '', '1', 1), ('ΑΠΟΘΝΗΙΣΚΩ', 22, 'αποθνῃσκω', '', '', '1', 1), ('ΑΠΟΚΡΙΝΩ', 23, 'αποκρινω', '', '', '1', 1), ('ΑΠΟΚΤΕΙΝΩ', 24, 'αποκτεινω', '', '', '1', 1), ('ΑΠΟΛΛΥΜΙ', 25, 'απολλυμι', '', '', '1', 1), ('ΑΡΕΤΗ', 26, 'αρετη', '', '', '1', 1), ('ΑΡΙΘΜΟΣ', 27, 'αριθμος', '', '', '1', 1), ('ΑΡΙΣΤΟΣ', 28, 'αριστος', '', '', '1', 1), ('ΑΡΧΗ', 29, 'αρχη', '', '', '1', 1), ('ΑΡΧΩ', 30, 'αρχω', '', '', '1', 1), ('ΑΡΧΩΝ', 31, 'αρχων', '', '', '1', 1), ('ΑΥΤΟΣ', 32, 'αυτος', '', '', '1', 1), ('ΒΑΙΝΩ', 33, 'βαινω', '', '', '1', 1), ('ΒΑΛΛΩ', 34, 'βαλλω', '', '', '1', 1), ('ΒΑΡΥΣ', 35, 'βαρυς', '', '', '1', 1), ('ΒΑΣΙΛΕΥΣ', 36, 'βασιλευς', '', '', '1', 1), ('ΒΕΛΤΙΩΝ', 37, 'βελτιων', '', '', '1', 1), ('ΒΙΟΣ', 38, 'βιος', '', '', '1', 1), ('ΒΛΕΠΩ', 39, 'βλεπω', '', '', '1', 1), ('ΒΟΥΛΕΥΩ', 40, 'βουλευω', '', '', '1', 1), ('ΒΟΥΛΟΜΑΙ', 41, 'βουλομαι', '', '', '1', 1), ('ΒΡΑΔΥΣ', 42, 'βραδυς', '', '', '1', 1), ('ΓΑΡ', 43, 'γαρ', '', '', '1', 1), ('ΓΕ', 44, 'γε', '', '', '1', 1), ('ΓΕΝΟΣ', 45, 'γενος', '', '', '1', 1), ('ΓΗ', 46, 'γη', '', '', '1', 1), ('ΓΙΓΝΟΜΑΙ', 47, 'γιγνομαι', '', '', '1', 1), ('ΓΙΓΝΩΣΚΩ', 48, 'γιγνωσκω', '', '', '1', 1), ('ΓΛΩΣΣΑ', 49, 'γλωσσα', '', '', '1', 1), ('ΓΝΩΜΗ', 50, 'γνωμη', '', '', '1', 1), ('ΓΡΑΜΜΑ', 51, 'γραμμα', '', '', '1', 1), ('ΓΡΑΦΗ', 52, 'γραφη', '', '', '1', 1), ('ΓΡΑΦΩ', 53, 'γραφω', '', '', '1', 1), ('ΓΥΝΗ', 54, 'γυνη', '', '', '1', 1), ('ΔΑΙΜΩΝ', 55, 'δαιμων', '', '', '1', 1), ('ΔΕ', 56, 'δε', '', '', '1', 1), ('ΔΕΙ', 57, 'δει', '', '', '1', 1), ('ΔΕΙΚΝΥΜΙ', 58, 'δεικνυμι', '', '', '1', 1), ('ΔΕΙΝΟΣ', 59, 'δεινος', '', '', '1', 1), ('ΔΕΣΠΟΤΗΣ', 60, 'δεσποτης', '', '', '1', 1), ('ΔΕΥΤΕΡΟΣ', 61, 'δευτερος', '', '', '1', 1), ('ΔΕΧΟΜΑΙ', 62, 'δεχομαι', '', '', '1', 1), ('ΔΗ', 63, 'δη', '', '', '1', 1), ('ΔΗΛΟΣ', 64, 'δηλος', '', '', '1', 1), ('ΔΗΛΟΩ', 65, 'δηλοω', '', '', '1', 1), ('ΔΗΜΟΣ', 66, 'δημος', '', '', '1', 1), ('ΔΙΑ', 67, 'δια', '', '', '1', 1), ('ΔΙΔΑΣΚΩ', 68, 'διδασκω', '', '', '1', 1), ('ΔΙΔΩΜΙ', 69, 'διδωμι', '', '', '1', 1), ('ΔΙΚΗ', 70, 'δικη', '', '', '1', 1), ('ΔΙΩΚΩ', 71, 'διωκω', '', '', '1', 1), ('ΔΟΚΕΙ', 72, 'δοκει', '', '', '1', 1), ('ΔΟΞΑ', 73, 'δοξα', '', '', '1', 1), ('ΔΟΥΛΟΣ', 74, 'δουλος', '', '', '1', 1), ('ΔΡΑΩ', 75, 'δραω', '', '', '1', 1), ('ΔΥΝΑΜΑΙ', 76, 'δυναμαι', '', '', '1', 1), ('ΔΥΝΑΜΙΣ', 77, 'δυναμις', '', '', '1', 1), ('ΕΑΝ', 78, 'εαν', '', '', '1', 1), ('ΕΓΩ', 79, 'εγω', '', '', '1', 1), ('ΕΘΕΛΩ', 80, 'εθελω', '', '', '1', 1), ('ΕΘΝΟΣ', 81, 'εθνος', '', '', '1', 1), ('ΕΙ', 82, 'ει', '', '', '1', 1), ('ΕΙΔΟΣ', 83, 'ειδος', '', '', '1', 1), ('ΕΙΜΙ', 84, 'ειμι', '', '', '1', 1), ('ΕΙΜΙ/2', 85, 'ειμι', '', '', '1', 1), ('ΕΙΠΟΝ', 86, 'ειπον,', '', '', '1', 1), ('ΕΙΡΗΝΗ', 87, 'ειρηνη', '', '', '1', 1), ('ΕΙΣ/2', 88, 'εις', '', '', '1', 1), ('ΕΚ', 89, 'εκ', '', '', '1', 1), ('ΕΚΑΣΤΟΣ', 90, 'εκαστος', '', '', '1', 1), ('ΕΚΕΙΝΟΣ', 91, 'εκεινος', '', '', '1', 1), ('ΕΛΑΣΣΩΝ', 92, 'ελασσων', '', '', '1', 1), ('ΕΛΑΥΝΩ', 93, 'ελαυνω', '', '', '1', 1), ('ΕΛΕΥΘΕΡΟΣ', 94, 'ελευθερος', '', '', '1', 1), ('ΕΛΠΙΣ', 95, 'ελπις', '', '', '1', 1), ('ΕΜΟΣ', 96, 'εμος', '', '', '1', 1), ('ΕΝ', 97, 'εν', '', '', '1', 1), ('ΕΠΙ', 98, 'επι', '', '', '1', 1), ('ΕΡΓΑΖΟΜΑΙ', 99, 'εργαζομαι', '', '', '1', 1), ('ΕΡΓΟΝ', 100, 'εργον', '', '', '1', 1), ('ΕΡΧΟΜΑΙ', 101, 'ερχομαι', '', '', '1', 1), ('ΕΡΩΤΑΩ', 102, 'ερωταω', '', '', '1', 1), ('ΕΤΕΡΟΣ', 103, 'ετερος', '', '', '1', 1), ('ΕΤΙ', 104, 'ετι', '', '', '1', 1), ('ΕΤΟΣ', 105, 'ετος', '', '', '1', 1), ('ΕΥΘΥΣ', 106, 'ευθυς', '', '', '1', 1), ('ΕΥΡΙΣΚΩ', 107, 'ευρισκω', '', '', '1', 1), ('ΕΧΘΡΟΣ/2', 108, 'εχθρος', '', '', '1', 1), ('ΕΧΩ', 109, 'εχω', '', '', '1', 1), ('ΖΑΩ', 110, 'ζαω', '', '', '1', 1), ('ΖΗΤΕΩ', 111, 'ζητεω', '', '', '1', 1), ('Η', 112, 'η', '', '', '1', 1), ('ΗΔΟΝΗ', 113, 'ηδονη', '', '', '1', 1), ('ΗΔΥΣ', 114, 'ηδυς', '', '', '1', 1), ('ΗΛΙΟΣ', 115, 'ηλιος', '', '', '1', 1), ('ΗΜΕΡΑ', 116, 'ημερα', '', '', '1', 1), ('ΗΜΕΤΕΡΟΣ', 117, 'ημετερος', '', '', '1', 1), ('ΗΣΣΩΝ', 118, 'ησσων', '', '', '1', 1), ('ΘΑΛΑΣΣΑ', 119, 'θαλασσα', '', '', '1', 1), ('ΘΑΝΑΤΟΣ', 120, 'θανατος', '', '', '1', 1), ('ΘΑΥΜΑΖΩ', 121, 'θαυμαζω', '', '', '1', 1), ('ΘΕΑ', 122, 'θεα', '', '', '1', 1), ('ΘΕΟΣ', 123, 'θεος', '', '', '1', 1), ('ΘΥΜΟΣ', 124, 'θυμος', '', '', '1', 1), ('ΙΑΤΡΟΣ', 125, 'ιατρος', '', '', '1', 1), ('ΙΗΜΙ', 126, 'ιημι', '', '', '1', 1), ('ΙΣΤΗΜΙ', 127, 'ιστημι', '', '', '1', 1), ('ΚΑΙ', 128, 'και', '', '', '1', 1), ('ΚΑΙΡΟΣ', 129, 'καιρος', '', '', '1', 1), ('ΚΑΚΟΣ', 130, 'κακος', '', '', '1', 1), ('ΚΑΛΕΩ', 131, 'καλεω', '', '', '1', 1), ('ΚΑΛΟΣ', 132, 'καλος', '', '', '1', 1), ('ΚΑΤΑ', 133, 'κατα', '', '', '1', 1), ('ΚΕΛΕΥΩ', 134, 'κελευω', '', '', '1', 1), ('ΚΕΦΑΛΗ', 135, 'κεφαλη', '', '', '1', 1), ('ΚΟΣΜΟΣ', 136, 'κοσμος', '', '', '1', 1), ('ΚΡΑΤΕΩ', 137, 'κρατεω', '', '', '1', 1), ('ΚΡΕΙΣΣΩΝ', 138, 'κρεισσων', '', '', '1', 1), ('ΚΡΙΝΩ', 139, 'κρινω', '', '', '1', 1), ('ΚΥΚΛΟΣ', 140, 'κυκλος', '', '', '1', 1), ('ΚΥΡΙΟΣ', 141, 'κυριος', '', '', '1', 1), ('ΚΩΛΥΩ', 142, 'κωλυω', '', '', '1', 1), ('ΛΑΛΕΩ', 143, 'λαλεω', '', '', '1', 1), ('ΛΑΜΒΑΝΩ', 144, 'λαμβανω', '', '', '1', 1), ('ΛΑΝΘΑΝΩ', 145, 'λανθανω', '', '', '1', 1), ('ΛΑΟΣ/2', 146, 'λαος', '', '', '1', 1), ('ΛΕΓΩ', 147, 'λεγω', '', '', '1', 1), ('ΛΕΙΠΩ', 148, 'λειπω', '', '', '1', 1), ('ΛΙΘΟΣ', 149, 'λιθος', '', '', '1', 1), ('ΛΟΓΟΣ', 150, 'λογος', '', '', '1', 1), ('ΛΥΩ', 151, 'λυω', '', '', '1', 1), ('ΜΑΚΡΟΣ', 152, 'μακρος', '', '', '1', 1), ('ΜΑΝΘΑΝΩ', 153, 'μανθανω', '', '', '1', 1), ('ΜΑΡΤΥΣ', 154, 'μαρτυς', '', '', '1', 1), ('ΜΑΧΗ', 155, 'μαχη', '', '', '1', 1), ('ΜΕΓΑΣ', 156, 'μεγας', '', '', '1', 1), ('ΜΕΛΛΩ', 157, 'μελλω', '', '', '1', 1), ('ΜΕΝ', 158, 'μεν', '', '', '1', 1), ('ΜΕΝΩ', 159, 'μενω', '', '', '1', 1), ('ΜΕΡΟΣ', 160, 'μερος', '', '', '1', 1), ('ΜΕΤΑ', 161, 'μετα', '', '', '1', 1), ('ΜΗ', 162, 'μη', '', '', '1', 1), ('ΜΗΤΗΡ', 163, 'μητηρ', '', '', '1', 1), ('ΜΙΚΡΟΣ', 164, 'μικρος', '', '', '1', 1), ('ΜΟΝΟΣ', 165, 'μονος', '', '', '1', 1), ('ΜΥΡΙΟΣ', 166, 'μυριος', '', '', '1', 1), ('ΝΑΟΣ', 167, 'ναος', '', '', '1', 1), ('ΝΙΚΑΩ', 168, 'νικαω', '', '', '1', 1), ('ΝΙΚΗ', 169, 'νικη', '', '', '1', 1), ('ΝΟΜΙΖΩ', 170, 'νομιζω', '', '', '1', 1), ('ΝΟΜΟΣ', 171, 'νομος', '', '', '1', 1), ('ΝΥΝ', 172, 'νυν', '', '', '1', 1), ('ΝΥΞ', 173, 'νυξ', '', '', '1', 1), ('ΞΕΝΟΣ', 174, 'ξενος', '', '', '1', 1), ('ΟΔΟΣ', 175, 'οδος', '', '', '1', 1), ('ΟΙΚΙΑ', 176, 'οικια', '', '', '1', 1), ('ΟΙΚΟΣ', 177, 'οικος', '', '', '1', 1), ('ΟΝΟΜΑ', 178, 'ονομα', '', '', '1', 1), ('ΟΞΥΣ', 179, 'οξυς', '', '', '1', 1), ('ΟΡΑΩ', 180, 'οραω', '', '', '1', 1), ('ΟΡΟΣ', 181, 'ορος', '', '', '1', 1), ('ΟΣ', 182, 'ος', '', '', '1', 1), ('ΟΤΙ', 183, 'οτι', '', '', '1', 1), ('ΟΥ', 184, 'ουκ', '', '', '1', 1), ('ΟΥΔΕΙΣ', 185, 'ουδεις', '', '', '1', 1), ('ΟΥΝ', 186, 'ουν', '', '', '1', 1), ('ΟΥΡΑΝΟΣ', 187, 'ουρανος', '', '', '1', 1), ('ΟΥΤΕ', 188, 'ουτε...ουτε', '', '', '1', 1), ('ΟΥΤΟΣ', 189, 'ουτος', '', '', '1', 1), ('ΟΥΤΩΣ', 190, 'ουτως', '', '', '1', 1), ('ΟΦΘΑΛΜΟΣ', 191, 'οφθαλμος', '', '', '1', 1), ('ΠΑΡΑ', 192, 'παρα', '', '', '1', 1), ('ΠΑΣ', 193, 'πας', '', '', '1', 1), ('ΠΑΣΧΩ', 194, 'πασχω', '', '', '1', 1), ('ΠΑΤΗΡ', 195, 'πατηρ', '', '', '1', 1), ('ΠΑΥΩ', 196, 'παυω', '', '', '1', 1), ('ΠΕΙΘΩ', 197, 'πειθω', '', '', '1', 1), ('ΠΕΙΡΑΩ', 198, 'πειραω', '', '', '1', 1), ('ΠΕΜΠΩ', 199, 'πεμπω', '', '', '1', 1), ('ΠΕΡΙ', 200, 'περι', '', '', '1', 1), ('ΠΙΠΤΩ', 201, 'πιπτω', '', '', '1', 1), ('ΠΙΣΤΕΥΩ', 202, 'πιστευω', '', '', '1', 1), ('ΠΙΣΤΙΣ', 203, 'πιστις', '', '', '1', 1), ('ΠΛΕΙΩΝ', 204, 'πλεων', '', '', '1', 1), ('ΠΝΕΥΜΑ', 205, 'πνευμα', '', '', '1', 1), ('ΠΟΙΕΩ', 206, 'ποιεω', '', '', '1', 1), ('ΠΟΙΗΤΗΣ', 207, 'ποιητης', '', '', '1', 1), ('ΠΟΙΟΣ/2', 208, 'ποιος', '', '', '1', 1), ('ΠΟΛΕΜΟΣ', 209, 'πολεμος', '', '', '1', 1), ('ΠΟΛΙΣ', 210, 'πολις', '', '', '1', 1), ('ΠΟΛΥΣ', 211, 'πολυς', '', '', '1', 1), ('ΠΟΝΗΡΟΣ', 212, 'πονηρος', '', '', '1', 1), ('ΠΟΡΕΥΩ', 213, 'πορευω', '', '', '1', 1), ('ΠΟΤΑΜΟΣ', 214, 'ποταμος', '', '', '1', 1), ('ΠΟΤΕΡΟΣ', 215, 'ποτερος', '', '', '1', 1), ('ΠΡΑΓΜΑ', 216, 'πραγμα', '', '', '1', 1), ('ΠΡΑΣΣΩ', 217, 'πρασσω', '', '', '1', 1), ('ΠΡΟΣ', 218, 'προς', '', '', '1', 1), ('ΠΡΟΣΩΠΟΝ', 219, 'προσωπον', '', '', '1', 1), ('ΠΡΩΤΟΣ', 220, 'πρωτος', '', '', '1', 1), ('ΠΥΡ', 221, 'πυρ', '', '', '1', 1), ('ΡΑΙΔΙΟΣ', 222, 'ῥᾳδιος', '', '', '1', 1), ('ΣΑΦΗΣ', 223, 'σαφης', '', '', '1', 1), ('ΣΚΟΠΕΩ', 224, 'σκοπεω', '', '', '1', 1), ('ΣΟΣ', 225, 'σος', '', '', '1', 1), ('ΣΟΦΟΣ', 226, 'σοφος', '', '', '1', 1), ('ΣΤΟΜΑ', 227, 'στομα', '', '', '1', 1), ('ΣΤΡΑΤΗΓΟΣ', 228, 'στρατηγος', '', '', '1', 1), ('ΣΤΡΑΤΙΩΤΗΣ', 229, 'στρατιωτης', '', '', '1', 1), ('ΣΥ', 230, 'συ', '', '', '1', 1), ('ΣΥΝ', 231, 'συν', '', '', '1', 1), ('ΣΩΖΩ', 232, 'σωζω', '', '', '1', 1), ('ΣΩΜΑ', 233, 'σωμα', '', '', '1', 1), ('ΣΩΤΗΡΙΑ', 234, 'σωτηρια', '', '', '1', 1), ('ΤΑΧΥΣ', 235, 'ταχυς', '', '', '1', 1), ('ΤΕ', 236, 'τε', '', '', '1', 1), ('ΤΕΚΝΟΝ', 237, 'τεκνον', '', '', '1', 1), ('ΤΕΛΟΣ', 238, 'τελος', '', '', '1', 1), ('ΤΕΜΝΩ', 239, 'τεμνω', '', '', '1', 1), ('ΤΕΧΝΗ', 240, 'τεχνη', '', '', '1', 1), ('ΤΙΘΗΜΙ', 241, 'τιθημι', '', '', '1', 1), ('ΤΙΚΤΩ', 242, 'τικτω', '', '', '1', 1), ('ΤΙΜΑΩ', 243, 'τιμαω', '', '', '1', 1), ('ΤΙΜΗ', 244, 'τιμη', '', '', '1', 1), ('ΤΙΣ', 245, 'τις', '', '', '1', 1), ('ΤΙΣ/2', 246, 'τις', '', '', '1', 1), ('ΤΟΠΟΣ', 247, 'τοπος', '', '', '1', 1), ('ΤΡΕΠΩ', 248, 'τρεπω', '', '', '1', 1), ('ΤΡΕΦΩ', 249, 'τρεφω', '', '', '1', 1), ('ΤΡΟΠΟΣ', 250, 'τροπος', '', '', '1', 1), ('ΤΥΓΧΑΝΩ', 251, 'τυγχανω', '', '', '1', 1), ('ΤΥΧΗ', 252, 'τυχη', '', '', '1', 1), ('ΥΔΩΡ', 253, 'υδωρ', '', '', '1', 1), ('ΥΙΟΣ', 254, 'υιος', '', '', '1', 1), ('ΥΠΑΡΧΩ', 255, 'υπαρχω', '', '', '1', 1), ('ΥΠΕΡ', 256, 'υπερ', '', '', '1', 1), ('ΥΠΟ', 257, 'υπο', '', '', '1', 1), ('ΦΑΙΝΩ', 258, 'φαινω', '', '', '1', 1), ('ΦΕΡΩ', 259, 'φερω', '', '', '1', 1), ('ΦΕΥΓΩ', 260, 'φευγω', '', '', '1', 1), ('ΦΗΜΙ', 261, 'φημι', '', '', '1', 1), ('ΦΙΛΟΣ/2', 262, 'φιλος', '', '', '1', 1), ('ΦΟΒΟΣ', 263, 'φοβος', '', '', '1', 1), ('ΦΡΟΝΕΩ', 264, 'φρονεω', '', '', '1', 1), ('ΦΥΛΑΣΣΩ', 265, 'φυλασσω', '', '', '1', 1), ('ΦΥΣΙΣ', 266, 'φυσις', '', '', '1', 1), ('ΦΥΩ', 267, 'φυω', '', '', '1', 1), ('ΦΩΝΗ', 268, 'φωνη', '', '', '1', 1), ('ΦΩΣ', 269, 'φως', '', '', '1', 1), ('ΧΑΙΡΩ', 270, 'χαιρω', '', '', '1', 1), ('ΧΑΛΕΠΟΣ', 271, 'χαλεπος', '', '', '1', 1), ('ΧΑΡΙΣ', 272, 'χαρις', '', '', '1', 1), ('ΧΕΙΡ', 273, 'χειρ', '', '', '1', 1), ('ΧΡΗ', 274, 'χρη', '', '', '1', 1), ('ΧΡΗΜΑ', 275, 'χρημα', '', '', '1', 1), ('ΧΡΟΝΟΣ', 276, 'χρονος', '', '', '1', 1), ('ΧΩΡΑ', 277, 'χωρᾱ', '', '', '1', 1), ('ΨΥΧΗ', 278, 'ψυχη', '', '', '1', 1), ('ΩΣ', 279, 'ως', '', '', '1', 1)]
section_list ={'1': 'start', 'end': '1', 'start': 'start'}
title = "National Collegiate Greek Exam Core"
section_level =  1
language = "Greek"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)