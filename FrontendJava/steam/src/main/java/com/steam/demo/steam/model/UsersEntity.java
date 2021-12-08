package com.steam.demo.steam.model;

import javax.persistence.*;

@Entity
@Table(name = "users", schema = "steam", catalog = "")
public class UsersEntity {
    private Integer id;
    private String nickname;
    private String profileLink;
    private String email;
    private Integer hoursPlayedLimit;

    @Id
    @Column(name = "id")
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    @Basic
    @Column(name = "nickname")
    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    @Basic
    @Column(name = "profile_link")
    public String getProfileLink() {
        return profileLink;
    }

    public void setProfileLink(String profileLink) {
        this.profileLink = profileLink;
    }

    @Basic
    @Column(name = "email")
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Basic
    @Column(name = "hours_played_limit")
    public Integer getHoursPlayedLimit() {
        return hoursPlayedLimit;
    }

    public void setHoursPlayedLimit(Integer hoursPlayedLimit) {
        this.hoursPlayedLimit = hoursPlayedLimit;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        UsersEntity that = (UsersEntity) o;

        if (id != null ? !id.equals(that.id) : that.id != null) return false;
        if (nickname != null ? !nickname.equals(that.nickname) : that.nickname != null) return false;
        if (profileLink != null ? !profileLink.equals(that.profileLink) : that.profileLink != null) return false;
        if (email != null ? !email.equals(that.email) : that.email != null) return false;
        if (hoursPlayedLimit != null ? !hoursPlayedLimit.equals(that.hoursPlayedLimit) : that.hoursPlayedLimit != null)
            return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = id != null ? id.hashCode() : 0;
        result = 31 * result + (nickname != null ? nickname.hashCode() : 0);
        result = 31 * result + (profileLink != null ? profileLink.hashCode() : 0);
        result = 31 * result + (email != null ? email.hashCode() : 0);
        result = 31 * result + (hoursPlayedLimit != null ? hoursPlayedLimit.hashCode() : 0);
        return result;
    }
}
