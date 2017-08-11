
/*
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * 2009 http://www.streamhead.com
 */

import java.io.FileInputStream;
import java.util.logging.Logger;

import javazoom.jl.player.Player;

/**
 * @author Peter Backx
 */
public class Main {

	static Logger log = Logger.getLogger("BeatIt");

	/**
	 * @param args
	 *            the command line arguments
	 */
	public static void main(String[] args) throws Exception {

		/// Neuer Code Abschnitt
		System.out.println(
				"Wie hoch ist ihre Herzfrequenz?" + "\nGeben Sie die Anzahl Ihres Herzschlages in einer Minute ein.");

		int Herzfrequenz;
		Herzfrequenz = StdIn.readInt();

		System.out.println("Vielen Dank! Legen Sie bitte die zu analysierende Musikdatei in den Ordner Analyse\n"
				+ "Geben Sie dann den Namen der Musikdatei ohne die Dateiendung .mp3 an");
		String liedname;
		liedname = StdIn.readString();
		// ____________________________________________________________

		BPM2SampleProcessor processor = new BPM2SampleProcessor();
		processor.setSampleSize(1024);
		EnergyOutputAudioDevice output = new EnergyOutputAudioDevice(processor);
		output.setAverageLength(1024);
		Player player = new Player(new FileInputStream("src/Analyse/" + liedname + ".mp3"), output);
		player.play();
		System.out.println("Der Beat pro Minute für diesen Song beträgt: " + processor.getBPM());

		int bpm = processor.getBPM();

		if (bpm > Herzfrequenz) {
			System.out.println("Dieser Song eignet sich, wenn Sie sich motivieren möchten.");
		} else {
			System.out.println("Dieser Song eignet sich, wenn Sie sich beruhigen möchten.");
		}
	}
}
