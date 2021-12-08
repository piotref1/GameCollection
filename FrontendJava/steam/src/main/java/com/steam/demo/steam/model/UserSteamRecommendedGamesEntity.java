package com.steam.demo.steam.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "user_steam_recommended_games", schema = "steam", catalog = "")
public class UserSteamRecommendedGamesEntity {
    private Integer id;
    private String title;
    private String has_achievements;
    private String achievements_percentage;
    private String genre;
    private String type;
    private Integer appid;



    @Id
    @Column(name = "id")
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }



    public String getHas_achievements() {
        return has_achievements;
    }

    public void setHas_achievements(String has_achievements) {
        this.has_achievements = has_achievements;
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        UserSteamRecommendedGamesEntity that = (UserSteamRecommendedGamesEntity) o;

        if (id != null ? !id.equals(that.id) : that.id != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        return id != null ? id.hashCode() : 0;
    }

    public Integer getAppid() {
        return appid;
    }

    public void setAppid(Integer appid) {
        this.appid = appid;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getAchievements_percentage() {
        return achievements_percentage;
    }

    public void setAchievements_percentage(String achievements_percentage) {
        this.achievements_percentage = achievements_percentage;
    }
    @Override
    public String toString() {
        return "UserSteamRecommendedGamesEntity{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", has_achievements='" + has_achievements + '\'' +
                ", achievements_percentage='" + achievements_percentage + '\'' +
                ", genre='" + genre + '\'' +
                ", type='" + type + '\'' +
                ", appid=" + appid +
                '}';
    }

}
