#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from match_text.match_clerk import get_clerk_name
from match_text.match_judge import get_judge_name
from xml_extractions.extract_node_values import Offset


def test_extract_judge_names():
    text1 = "sera jugé par Madame Bingo TOTO, Conseiller près la cour de machin chose"
    assert get_judge_name(text1) == [Offset(21, 31, "JUDGE_CLERK_1")]
    text2 = "Monsieur Gilles BOURGEOIS, Conseiller faisant fonction de Président"
    assert get_judge_name(text2) == [Offset(9, 25, "JUDGE_CLERK_1")]
    text3 = "Nous, Gilles BOURGEOIS, Conseiller faisant fonction de Président"
    assert get_judge_name(text3) == [Offset(6, 22, "JUDGE_CLERK_1")]
    text4 = "Mme Véronique BEBON, Présidente"
    assert get_judge_name(text4) == [Offset(4, 19, "JUDGE_CLERK_1")]
    text5 = "M. Gérard FORET DODELIN, Président"
    assert get_judge_name(text5) == [Offset(3, 23, "JUDGE_CLERK_1")]
    text6 = "Madame Florence DELORD, Conseiller"
    assert get_judge_name(text6) == [Offset(7, 22, "JUDGE_CLERK_1")]
    text7 = "Madame Frédérique BRUEL, Conseillère"
    assert get_judge_name(text7) == [Offset(7, 23, "JUDGE_CLERK_1")]
    text8 = "devant M. Gérard FORET DODELIN, Président, chargé d'instruire l'affaire."
    assert get_judge_name(text8) == [Offset(10, 30, "JUDGE_CLERK_1")]
    text9 = "représenté lors des débats par Madame POUEY, substitut général "
    assert get_judge_name(text9) == [Offset(38, 43, "JUDGE_CLERK_1")]
    text10 = "devant Mme Véronique BEBON, Présidente, et Madame Frédérique BRUEL, Conseillère, chargées du rapport."
    assert get_judge_name(text10) == [Offset(11, 26, "JUDGE_CLERK_1"), Offset(50, 66, "JUDGE_CLERK_1")]
    text11 = "Mme Geneviève TOUVIER, présidente"
    assert get_judge_name(text11) == [Offset(4, 21, "JUDGE_CLERK_1")]
    text12 = "Monsieur Michel WACHTER, conseiller,"
    assert get_judge_name(text12) == [Offset(9, 23, "JUDGE_CLERK_1")]
    text13 = "- Michel FICAGNA, conseiller"
    assert get_judge_name(text13) == [Offset(2, 16, "JUDGE_CLERK_1")]
    text14 = "Audience tenue par Florence PAPIN, conseiller, faisant "
    assert get_judge_name(text14) == [Offset(19, 33, "JUDGE_CLERK_1")]
    text15 = "Vincent NICOLAS, Conseiller"
    assert get_judge_name(text15) == [Offset(0, 15, "JUDGE_CLERK_1")]
    text16 = "2016, Monsieur Hubert de BECDELIEVRE, président de chambre"
    assert get_judge_name(text16) == [Offset(15, 36, "JUDGE_CLERK_1")]
    text17 = "Conseiller : Mélanie FILIATREAU"
    assert get_judge_name(text17) == [Offset(13, 31, "JUDGE_CLERK_1")]
    text18 = "Présidente : Mme Mélanie FILIATREAU"
    assert get_judge_name(text18) == [Offset(17, 35, "JUDGE_CLERK_1")]
    text19 = "Monsieur Benoît HOLLEAUX, conseiller faisant fonction de président"
    assert get_judge_name(text19) == [Offset(9, 24, "JUDGE_CLERK_1")]
    text20 = "Présidée par Isabelle BORDENAVE, Conseiller, magistrat rapporteur, qui en a rendu compte à la Cour."
    assert get_judge_name(text20) == [Offset(13, 31, "JUDGE_CLERK_1")]
    text21 = "Madame Françoise AYMES BELLADINA, conseiller faisant fonction de président de chambre"
    assert get_judge_name(text21) == [Offset(7, 32, "JUDGE_CLERK_1")]
    text22 = "outre elle même, de Daniel TROUVE, premier président, et "
    assert get_judge_name(text22) == [Offset(20, 33, "JUDGE_CLERK_1")]
    text23 = "Nous, Françoise GILLY ESCOFFIER, Conseiller de la Mise en Etat de la 10e Chambre de la Cour d'Appel " \
             "d'Aix en Provence, assistée de GENEVIÈVE JAUFFRES, Greffier"
    assert get_judge_name(text23) == [Offset(6, 31, "JUDGE_CLERK_1")]
    text24 = "Nous, Anne VIDAL, Magistrat de la Mise en Etat de la 6e Chambre D de la Cour D'appel D'aix En Provence, " \
             "assisté de Dominique COSTE, Greffier,"
    assert get_judge_name(text24) == [Offset(6, 16, "JUDGE_CLERK_1")]
    text25 = "Monsieur Gilles BOURGEOIS, Conseiller faisant fonction de Président"
    assert get_judge_name(text25) == [Offset(9, 25, "JUDGE_CLERK_1")]
    text26 = "Signé par Madame Laure BOURREL, Président et Madame Priscilla BOSIO, Greffier, auquel la minute de" \
             " la décision a été remise par le magistrat signataire.    "
    assert get_judge_name(text26) == [Offset(17, 30, "JUDGE_CLERK_1")]


def test_extract_clerk_names():
    text = "Madame To TOTO, greffier"
    assert get_clerk_name(text) == [Offset(7, 14, "JUDGE_CLERK_1")]
    text2 = "assistée de Geneviève JAUFFRES, greffier"
    assert get_clerk_name(text2) == [Offset(12, 30, "JUDGE_CLERK_1")]
    text3 = "Cour d'Appel d'Aix en Provence, assisté de Josiane BOMEA, Greffier "
    assert get_clerk_name(text3) == [Offset(43, 56, "JUDGE_CLERK_1")]
    text4 = "Greffier lors des débats : Veronique SAIGE"
    assert get_clerk_name(text4) == [Offset(27, 42, "JUDGE_CLERK_1")]
    text5 = "Greffier lors des débats : Madame Françoise PARADIS DEISS."
    assert get_clerk_name(text5) == [Offset(34, 57, "JUDGE_CLERK_1")]
    text6 = "assistée de Geneviève JAUFFRES, greffière"
    assert get_clerk_name(text6) == [Offset(12, 30, "JUDGE_CLERK_1")]
    text7 = "GREFFIER : Mme Marie Estelle CHAPON"
    assert get_clerk_name(text7) == [Offset(15, 35, "JUDGE_CLERK_1")]
    text8 = 'Arrêt signé par Monsieur LE GALLO, Président et par Madame HAON, Greffier.'
    assert get_clerk_name(text8) == [Offset(59, 63, "JUDGE_CLERK_1")]
    text9 = "Signé par Madame Laure BOURREL, Président et Madame Priscilla BOSIO, Greffier, auquel la minute " \
            "de la décision a été remise par le magistrat signataire.    "
    assert get_clerk_name(text9) == [Offset(52, 67, 'JUDGE_CLERK_1')]
