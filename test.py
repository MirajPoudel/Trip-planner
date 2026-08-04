from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import  run_travel_agent
# res = search_flights("plan a 7days bangladesh trip from nepal")
# print(res)

res = run_travel_agent()
print(res)