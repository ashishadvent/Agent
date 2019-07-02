Feature: WLA agent Installer test set

  
  Scenario: Install WLA to default location
      Given dotnet pre-requisite check
      when install WLA agent at default location
      when WLA agent is installed at default location
      then Enable WLA Agent at default location
      then Primary SAS Configuration at default location
      then Server Status check at default location
      then Authentication Test at default location
      then Disable WLA at default location
      then Remove WLA agent

