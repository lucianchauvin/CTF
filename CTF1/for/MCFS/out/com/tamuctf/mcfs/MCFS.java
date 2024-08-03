package com.tamuctf.mcfs;

import org.bukkit.plugin.java.JavaPlugin;

public class MCFS extends JavaPlugin {
  public void onEnable() { 
      getCommand("write").setExecutor(new CommandWrite()); 
      getCommand("unwrite").setExecutor(new CommandUnwrite()); 
  }
  
  public void onDisable() {}
}
