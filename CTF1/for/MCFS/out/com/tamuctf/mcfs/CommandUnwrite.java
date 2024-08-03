
package com.tamuctf.mcfs;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Iterator;
import org.bukkit.GameRule;
import org.bukkit.Material;
import org.bukkit.Tag;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.*;
import org.bukkit.Server;
import org.bukkit.plugin.java.JavaPlugin;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class CommandUnwrite implements CommandExecutor {
  public static final int CHUNKSIZE = 16;
  
  public static final int CHUNKHEIGHT = 256;
  
  public static final int BLOCKLEN = 16;
  
  public static final int X = 0;
  
  public static final int Z = 0;
  
  public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
    ((Player)sender).getWorld().setGameRule(GameRule.DO_DAYLIGHT_CYCLE, Boolean.valueOf(false));
    ((Player)sender).getWorld().setGameRule(GameRule.RANDOM_TICK_SPEED, Integer.valueOf(0));
    Hashtable<Integer, Tag<Material>> tagBlacklist = new Hashtable<Integer, Tag<Material>>();
    Hashtable<Tag<Material>, Integer> revtagBlacklist = new Hashtable<Tag<Material>, Integer>();
    tagBlacklist.put(Integer.valueOf(1), Tag.ENDERMAN_HOLDABLE);
    tagBlacklist.put(Integer.valueOf(2), Tag.BAMBOO_PLANTABLE_ON);
    tagBlacklist.put(Integer.valueOf(4), Tag.SNOW);
    Hashtable<Integer, Material> materialHashMap = new Hashtable<Integer, Material>();
    Hashtable<Material, Integer> rmaterialHashMap = new Hashtable<Material, Integer>();
    Iterator<Material> materials = Arrays.stream(Material.values()).iterator();
    int i = 0;
    while (materialHashMap.size() < 256 && materials.hasNext()) {
      Material material = (Material)materials.next();
      if (material.isSolid() && !material.hasGravity() && 
        !material.isInteractable() && !material.equals(Material.FARMLAND) && 
        !isTagged(tagBlacklist, material)) {
        materialHashMap.put(Integer.valueOf(i), material);
        rmaterialHashMap.put(material, Integer.valueOf(i));
        i++;
      } 
    } 
        FileWriter fstream = null;
    try {
        fstream = new FileWriter("data"); 
    } catch (IOException e) {
          e.printStackTrace();
    } 
    int byteIndex = 0;
    int row = 0;
    try {
      while (true) {
        for (int x = 0; x < 256; x++) {
          for (int y = 0; y < 256; y++) {
            for (int z = 0; z < 16; z++) {
                byteIndex += 1;
System.out.println(x + " " + y + " " +z + " " + byteIndex);
               fstream.write(rmaterialHashMap.get(((Player)sender).getWorld().getBlockAt(0 + x, 256 - y, 0 + 16 * row + z).getType()));
            } 
          } 
        } 
        row++;
      } 
    } catch (Exception e) {
      e.printStackTrace();
        System.out.println(byteIndex) ;
      return true;
    } 
  }
  
  private boolean isTagged(Hashtable<Integer, Tag<Material>> blacklist, Material material) {
    Enumeration<Integer> e = blacklist.keys();
    while (e.hasMoreElements()) {
      int key = ((Integer)e.nextElement()).intValue();
      if (((Tag)blacklist.get(Integer.valueOf(key))).isTagged(material))
        return true; 
    } 
    return false;
  }
}
