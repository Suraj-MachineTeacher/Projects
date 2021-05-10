select *
From PortfolioProject..CovidData
Order by 3,4	

Select location,date, total_cases,new_cases, total_deaths, population
From PortfolioProject..CovidData
order by 1,2


-- Shwows likelihood of Dying if you contract covid in your country
Select Location, date, total_cases, total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject..CovidData
Where Location like 'India'
order by 1,2

-- Looking at Total cases and the population
-- Shows what percentage of population got covid
Select Location, date,population, total_cases,(total_cases/population)*100 as Percent of PopulationInfected
From PortfolioProject..CovidData
--Where Location like 'India'
order by 1,2



--Looking at Countries with Highest Infection Rate compared to Population
Select Location,population, Max(total_cases)as HighestInfectionCount,Max(total_cases/population)*100 as PercentPopulationInfected
From PortfolioProject..CovidData
--Where Location like 'India'
group by location, population
order by PercentPopulationInfected desc




-- Countries with highest death count per population
Select Location,MAX(cast(Total_deaths as int)) as Total_Death_Count
From PortfolioProject..CovidData
Where continent is not null
--Where Location like 'India'
group by location
order by Total_Death_Count desc

--Lets break things down by continent
Select Location,MAX(cast(Total_deaths as int)) as Total_Death_Count
From PortfolioProject..CovidData
Where continent is null
group by location
order by Total_Death_Count desc

--Showing continents with the highest death count per population
Select continent,MAX(cast(Total_deaths as int)) as Total_Death_Count
From PortfolioProject..CovidData
Where continent is not null
group by continent
order by Total_Death_Count desc

--Global Numbers
Select date, SUM(new_cases) as Total_New_Cases , SUM(cast(new_deaths as int)) as Total_new_deaths , (SUM(cast(new_deaths as int))/SUM(new_cases))* 100 as Percentages_deaths
from PortfolioProject..CovidData
Group by date
Order by Total_new_deaths desc
offset 0 rows
fetch first 10 rows only


Select  SUM(new_cases) as Total_New_Cases , SUM(cast(new_deaths as int)) as Total_new_deaths , (SUM(cast(new_deaths as int))/SUM(new_cases))* 100 as Percentages_deaths
from PortfolioProject..CovidData
Where continent is not null
Order by Total_new_deaths desc