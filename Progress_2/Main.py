from searchagent import SearchAgent
from problems import SingleFoodProblem,MutilFoodProblem

problemInput = input("Enter Problem (Single or Multi) ")
if problemInput.lower()=='single':
  problem = SingleFoodProblem()
elif problemInput.lower()=='multi':
  problem = MutilFoodProblem()

fileinput = input("Enter file name ")
problem.load_input_pacman(fileinput)

agent = SearchAgent()
pickedalgorithm = input("Enter algorithm ")

if pickedalgorithm == "bfs":
  res = agent.bfs(problem)
  problem.animate(res)
elif pickedalgorithm == "dfs":
  res = agent.dfs(problem)
  problem.animate(res)
elif pickedalgorithm == "ucs":
  res = agent.ucs(problem)
  problem.animate(res)
