package com.steam.demo.steam.model;

import javax.persistence.*;

@Entity
@Table(name = "steam_games", schema = "steam", catalog = "")
public class SteamGamesEntity {
    private Integer appid;
    private String title;
    private Byte hasAchievements;
    private String genre;
    private Long id;
    private String achievements;
    private Long gameId;
    private String timePlayed;
    private Long userId;

    @Id
    @Column(name = "appid")
    public Integer getAppid() {
        return appid;
    }

    public void setAppid(Integer appid) {
        this.appid = appid;
    }

    @Basic
    @Column(name = "title")
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    @Basic
    @Column(name = "has_achievements")
    public Byte getHasAchievements() {
        return hasAchievements;
    }

    public void setHasAchievements(Byte hasAchievements) {
        this.hasAchievements = hasAchievements;
    }

    @Basic
    @Column(name = "genre")
    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    @Basic
    @Column(name = "id")
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Basic
    @Column(name = "achievements")
    public String getAchievements() {
        return achievements;
    }

    public void setAchievements(String achievements) {
        this.achievements = achievements;
    }

    @Basic
    @Column(name = "game_id")
    public Long getGameId() {
        return gameId;
    }

    public void setGameId(Long gameId) {
        this.gameId = gameId;
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
    @Column(name = "user_id")
    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        SteamGamesEntity that = (SteamGamesEntity) o;

        if (appid != null ? !appid.equals(that.appid) : that.appid != null) return false;
        if (title != null ? !title.equals(that.title) : that.title != null) return false;
        if (hasAchievements != null ? !hasAchievements.equals(that.hasAchievements) : that.hasAchievements != null)
            return false;
        if (genre != null ? !genre.equals(that.genre) : that.genre != null) return false;
        if (id != null ? !id.equals(that.id) : that.id != null) return false;
        if (achievements != null ? !achievements.equals(that.achievements) : that.achievements != null) return false;
        if (gameId != null ? !gameId.equals(that.gameId) : that.gameId != null) return false;
        if (timePlayed != null ? !timePlayed.equals(that.timePlayed) : that.timePlayed != null) return false;
        if (userId != null ? !userId.equals(that.userId) : that.userId != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = appid != null ? appid.hashCode() : 0;
        result = 31 * result + (title != null ? title.hashCode() : 0);
        result = 31 * result + (hasAchievements != null ? hasAchievements.hashCode() : 0);
        result = 31 * result + (genre != null ? genre.hashCode() : 0);
        result = 31 * result + (id != null ? id.hashCode() : 0);
        result = 31 * result + (achievements != null ? achievements.hashCode() : 0);
        result = 31 * result + (gameId != null ? gameId.hashCode() : 0);
        result = 31 * result + (timePlayed != null ? timePlayed.hashCode() : 0);
        result = 31 * result + (userId != null ? userId.hashCode() : 0);
        return result;
    }
}
