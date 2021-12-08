package com.steam.demo.steam.repository;


import com.steam.demo.steam.model.UserSteamStatisticsEntity;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository("steamStatistics")
public interface UserSteamStatisticsRepository extends CrudRepository<UserSteamStatisticsEntity, Integer> {

    public Iterable<UserSteamStatisticsEntity> findAll();


    @Query(value = "select sg.genre, count(*) as amount from user_steam_games usg join steam_games sg on usg.game_id=appid where usg.user_id=? and sg.genre!='None' group by sg.genre order by count(*) DESC;",
            nativeQuery = true)
    List<List<Object>> findFilled(Integer user_id);



}