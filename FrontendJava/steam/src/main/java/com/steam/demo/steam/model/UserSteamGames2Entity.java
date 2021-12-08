package com.steam.demo.steam.model;

import javax.persistence.*;

@Entity
@Table(name = "user_steam_games", schema = "steam", catalog = "")
public class UserSteamGames2Entity {

    private String id;
    private String user_id;
    private String game_id;
    private String title;
    private String timePlayed;
    private String achievements;


    @Id
    @Column(name = "id")
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


    @Basic
    @Column(name = "time_played")
    public String getTimePlayed() {
        return timePlayed;
    }

    public void setTimePlayed(String timePlayed) {
        this.timePlayed = timePlayed;
    }

    @Basic
    @Column(name = "achievements")
    public String getAchievements() {
        return achievements;
    }

    public void setAchievements(String achievements) {
        this.achievements = achievements;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getGame_id() {
        return game_id;
    }

    public void setGame_id(String game_id) {
        this.game_id = game_id;
    }

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }

    @Override
    public String toString() {
        return "UserSteamGames2Entity{" +
                "user_id='" + user_id + '\'' +
                ", game_id='" + game_id + '\'' +
                ", title='" + title + '\'' +
                ", timePlayed='" + timePlayed + '\'' +
                ", achievements='" + achievements + '\'' +
                '}';
    }
}
