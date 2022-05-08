package game;

import java.util.Random;

public class Spawn {
	private Handler handler;
	private HUD hud;
	
	public static int timer = 0;
	private Random r;
	
	public Spawn(Handler handler, HUD hud) {
		this.handler = handler;
		this.hud = hud;
		
		r = new Random();
	}
	
	public void tick() {
		timer++;
		
		if (timer >= 300) {
			timer = 0;
			GameObject a = handler.object.getFirst();
			ID b = a.getId();
			handler.removeObject(a);
			if (b == ID.easy) {
				handler.addObject(new Target(r.nextInt(Game.WIDTH -128), r.nextInt(Game.HEIGHT -128), ID.easy, handler));
			} else if(b == ID.medium) {
				handler.addObject(new Target(r.nextInt(Game.WIDTH -64), r.nextInt(Game.HEIGHT -64), ID.easy, handler));
			} else {
				handler.addObject(new Target(r.nextInt(Game.WIDTH -32), r.nextInt(Game.HEIGHT -32), ID.easy, handler));
			}
			
		}
	}
}
