package com.steam.demo.steam.repository;

import com.steam.demo.steam.model.UserSteamGames2Entity;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository("steamGamesRepository")
public interface SteamGamesRepository extends CrudRepository<UserSteamGames2Entity, Integer> {

    public Iterable<UserSteamGames2Entity> findAll();


    @Query(value = "select usg.id,usg.game_id, usg.user_id, sg.title,usg.time_played,usg.achievements from user_steam_games usg join steam_games sg on usg.game_id=sg.appid where usg.user_id =?;",
            nativeQuery = true)
    List<UserSteamGames2Entity> findFilled(Integer user_id);



}