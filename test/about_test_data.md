# Testdaten

Für die automatischen Unittests in diesem Package wird eine Testschar benötigt. Aktuell ist es [diese](https://jubla.puzzle.ch/groups/680).

Sie kann wie folgt eingerichtet werden:

1. Auf der jubla.db Testumgebung eine Schar erstellen
2. In der Schar eine neue Person erfassen und dieser Schar als Rolle "Scharleitung" hinzufügen
   - Vorname: API
   - Nachname: Test1
3. Die neue Person imitieren
4. Im Info-Tab auf "API-Keys"
5. Neuer API-Key erstellen
   - Zugriffsbereich: Lese- und Schreibrechte auf dieser und darunterliegenden Ebenen
   - Rechte: alle

Der API-Key muss in der Umgebungsvariable `JUBLADB_API_KEY` den Tests zur Verfügung gestellt werden.