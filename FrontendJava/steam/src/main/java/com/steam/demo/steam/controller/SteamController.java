
package com.steam.demo.steam.controller;

import com.steam.demo.steam.repository.SteamGamesRepository;
import com.steam.demo.steam.repository.UserSteamRecommendedRepository;
import com.steam.demo.steam.repository.UserSteamStatisticsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class SteamController {

    @Qualifier("steamGamesRepository")
    @Autowired
    private SteamGamesRepository steamGames;

    @Qualifier("steamGamesSuggestions")
    @Autowired
    private UserSteamRecommendedRepository steamSuggestedGames;

    @Autowired
    private UserSteamStatisticsRepository steamStatistics;

    @GetMapping("/")
    public String getNews() {

        return "index";
    }

    @GetMapping("/steamgames/{id}")
    public String getGameList(Model model, @PathVariable("id") Integer id) {

        model.addAttribute("steamgames", steamGames.findFilled(id));
        return "steamgames";
    }

    @GetMapping("/suggestions/{id}")
    public String getSuggestionsPage(Model model,@PathVariable("id") Integer id) {

        model.addAttribute("toBuySuggestions", steamSuggestedGames.findFilled(id,"Buy"));
        model.addAttribute("toFinishSuggestions", steamSuggestedGames.findFilled(id,"Finish"));
        model.addAttribute("toPlaySuggestions", steamSuggestedGames.findFilled(id,"Play"));
        return "suggestions";
    }

    @GetMapping("/statistics/{id}")
    public String getStatisticsPage(Model model, @PathVariable("id") Integer id) {

        model.addAttribute("statistics", steamStatistics.findFilled(id));
        return "statistics";
    }

}
