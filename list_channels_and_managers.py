from KalturaClient import *
from KalturaClient.Plugins.Core import *
import math

config = KalturaConfiguration()
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
    "<secret>",
    "<user>",
    KalturaSessionType.ADMIN,
    < pid >)
client.setKs(ks)

filterCat = KalturaCategoryFilter()
filterCat.fullNameStartsWithIn = "MediaSpace>site>channels"
filterCat.depthEqual = 3
pagerCat = KalturaFilterPager()
pagerUser = KalturaFilterPager()
pagerCat.pageSize = 30
pagerUser.pageSize = 30
filterUser = KalturaCategoryUserFilter()
filterUser.permissionLevelEqual = KalturaCategoryUserPermissionLevel.MANAGER

print('CHANNEL_ID\tCHANNEL_NAME\tCHANNEL_OWNER\tCHANNEL_ENTRIES_COUNT\tCHANNEL_USERS_COUNT\tCHANNEL_MANAGER')
resultCat = client.category.list(filterCat, pagerCat)
for pagerCat.pageIndex in range(1, math.ceil(resultCat.totalCount/pagerCat.pageSize)+1):
    resultCat = client.category.list(filterCat, pagerCat)
    for cat in resultCat.getObjects():
        filterUser.categoryIdEqual = cat.id

        resultUser = client.categoryUser.list(filterUser, pagerUser)
        for pagerUser.pageIndex in range(1, math.ceil(resultUser.totalCount/pagerUser.pageSize)+1):
            for user in resultUser.getObjects():
                print(cat.id, '\t', cat.name, '\t', cat.owner, '\t',
                      cat.entriesCount, '\t', cat.membersCount, '\t', user.userId)
