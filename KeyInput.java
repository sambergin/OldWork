package game;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Random;

import game.Game.STATE;



public class KeyInput extends KeyAdapter {
	

	private Game game;
	public String s;
	public int timer;
	public int rel_time;
	public int score;
	private Random r;
	
	public KeyInput(Game game) {
		this.game = game;
		s = "";
		r = new Random();
		timer = 60*100;
		rel_time = 0;
		score = 0;
	}
	
	public String selStr() {
		String a = game.strArr.get(r.nextInt(game.strArr.size()));
		return a;
	}
	
	public void reset() {
		s = "";
		timer = 60*100;
		rel_time = 0;
		score = 0;
		game.userIn.setText(s);
		game.userOut.setText(selStr());
	}
	
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		
		if(key == KeyEvent.VK_ESCAPE) {

			if (game.gameState == STATE.MouseGame) {
				game.gameState = STATE.MPauseMenu;
			} else if (game.gameState == STATE.TypeGame) {
				game.gameState = STATE.TPauseMenu;
			} else if (game.gameState == STATE.MPauseMenu) {
				game.gameState = STATE.MouseGame;
			} else if (game.gameState == STATE.TPauseMenu) {
				game.gameState = STATE.TypeGame;
			}

		}  else if (key == KeyEvent.VK_ENTER) {
			//Comp string, add points
			if (game.userIn.getText().equals(game.userOut.getText())) {
				score += 100 - (rel_time/10);
			}
			game.userOut.setText(selStr());
			rel_time = 0;
			s = "";
			game.userIn.setText(s);//update text string
			
		}
		else if (key == KeyEvent.VK_BACK_SPACE) {
			//Backspace string
			s = s.substring(0, s.length()-1);
			game.userIn.setText(s);//update text string
			
		}
	}
	public void keyReleased(KeyEvent e) {
		
	}
	
	public void keyTyped(KeyEvent e) {
		char t = e.getKeyChar();
		//Only accepts characters that can be in the string (alphabet, comma, period, round and square brackets)
		if (t == 32 || t == 33 || t == 40 || t == 41 || t == 44 || t == 46 || (t>64 && t<90) || t == 91 || t == 93 || (t>96 && t<123)) {
			s = s + t;
			game.userIn.setText(s);//update text string
		}
	}
	
	public void tick() {
		timer--;
		rel_time++;
		if (timer == 0) { //Game over
			game.gameState = STATE.TypeEndMenu;
		}
	}
	
	public void render(Graphics g) {
		Font font = new Font("arial",1,20);
		Font titl = new Font("arial",1,40);
		g.setFont(titl);
		g.setColor(Color.CYAN);
		g.drawString("Type this phrase... FAST!", Game.WIDTH/2-240, 50);
		g.setFont(font);
		g.setColor(Color.MAGENTA);
		g.fillRect(Game.WIDTH/2-400, 100, 800, 64);
		g.setColor(Color.YELLOW);
		g.drawString(game.userOut.getText(), Game.WIDTH/2-390, 140);
		g.setColor(Color.ORANGE);
		g.fillRect(Game.WIDTH/2-400, 300, 800, 64);
		g.setColor(Color.MAGENTA);
		g.drawString(game.userIn.getText(),  Game.WIDTH/2-390, 340);
		g.drawString("Time Left: " + timer /100, 0, 500);
		g.drawString("Time Taken on This Phrase: " + rel_time/100, 0, 550);
		g.drawString("Score: " + score, 0, 600);
		
		
	}
}
