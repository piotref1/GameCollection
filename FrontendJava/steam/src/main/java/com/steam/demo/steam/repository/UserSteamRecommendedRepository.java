package com.steam.demo.steam.repository;

import com.steam.demo.steam.model.UserSteamRecommendedGamesEntity;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository("steamGamesSuggestions")
public interface UserSteamRecommendedRepository extends CrudRepository<UserSteamRecommendedGamesEntity, Integer> {

    public Iterable<UserSteamRecommendedGamesEntity> findAll();


    @Query(value = "SELECT sg.appid, usrg.type, sg.title, sg.has_achievements, usg.achievements_percentage, sg.genre \n" +
            "FROM user_steam_recommended_games usrg \n" +
            "left JOIN user_steam_games usg ON usg.game_id= usrg.game_id and usg.user_id = usrg.user_id\n" +
            "left JOIN steam_games sg ON sg.appid=usrg.game_id where usrg.user_id=? and usrg.type=?;",
            nativeQuery = true)
    List<List<Object>> findFilled(Integer user_id, String type);

}