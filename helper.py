import requests


def get_leetcode(query, username):
  ENDPOINT = 'https://leetcode.com/graphql/'
  headers = {
  }
  variables = {
    'username': username
  }
  json_data = {
    'query': query,
    'variables': variables
  }
  
  resp = requests.post(ENDPOINT, json=json_data)
  
  return resp.json()['data']

def get_profile(username):
  query_profile = """
  query userPublicProfile($username: String!) {
    matchedUser(username: $username) {
      username
      githubUrl
      twitterUrl
      linkedinUrl
      profile {
        ranking
        userAvatar
        realName
        aboutMe
        school
        websites
        countryName
        company
        jobTitle
        skillTags
        postViewCount
        postViewCountDiff
        reputation
        reputationDiff
        solutionCount
        solutionCountDiff
        categoryDiscussCount
        categoryDiscussCountDiff
      }
    }
  }"""
  
  raw_data = get_leetcode(query_profile, username)
  user_data = raw_data['matchedUser']
  
  return user_data

def get_problems(username = None):
  query_problems = """
    query userProblemsSolved($username: String!) {
    allQuestionsCount {
      difficulty
      count
    }
    matchedUser(username: $username) {
      problemsSolvedBeatsStats {
        difficulty
        percentage
      }
      submitStatsGlobal {
        acSubmissionNum {
          difficulty
          count
        }
      }
    }
  }"""
  
  return get_leetcode(query_problems, username)

if __name__ == '__main__':
  print(get_profile('josephma293'))
  print(get_problems('josephma293'))