<template>
  <div class="upcoming-list-wrap">
    <v-expansion-panels accordion flat>
      <v-expansion-panel v-for="item in events" :key="item.id">
        <v-expansion-panel-header expand-icon="mdi-chevron-down">
          <template>
            <v-row no-gutters>
              <v-row no-gutters>
                <v-col cols="2"
                  ><span class="item-date">
                    <div class="item-date_left">{{ item.date }}</div>
                    <div class="item-date_right">
                      <div class="item-date_right_day">{{ item.day }}</div>
                      <div class="item-date_right_month">{{ item.month }}</div>
                    </div>
                  </span></v-col
                >
                <v-col class="item-artist">{{ item.name }}</v-col>
              </v-row>
              <v-col class="item-link">
                <button class="link-btn" @click="toEventPage(item.id)">
                  VIEW MORE
                </button>
              </v-col>
            </v-row>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <div class="item-des-time">
            {{ item.date + " " + item.month + ", " + item.time }}
          </div>
          <div class="item-des-location">{{ item.location }}</div>
          <div class="item-description">
            {{ item.description }}
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  data() {
    return {
      events: [
        {
          id: 3,
          name: "John Smith",
          day: "Thu",
          date: "23",
          month: "Apr",
          time: "2:00AM",
          location: "Streaming LIVE - Live in Chester",
          description:
            "John Smith is told almost every day that he has the most common name in the world. However, other than the name, there is nothing commonplace about him. John has played to audiences all over the world, in living rooms, festival tents and sold-out concert halls. He tours relentlessly with a guitar and a suitcase, sometimes with a small band, always looking to communicate through a song and to share something intangible with those willing to listen.",
        },
        {
          id: 4,
          name: "Enamour",
          day: "Thu",
          date: "23",
          month: "Apr",
          time: "3:00AM",
          location: "Streaming LIVE",
          description:
            "As a curator of infectious grooves and wistful atmospheres, Enamour has developed a sound that delicately walks the line between deep introspection and pure club play. His sets are an intricate blend of deep, progressive, tech house and techno that values musicality over anything else.",
        },
        {
          id: 1,
          name: "Hayley Wilson",
          day: "Thu",
          date: "23",
          month: "Apr",
          time: "7:00PM",
          location: "Streaming LIVE",
          description:
            "Hayley Wilson is a modern songstress whose light, effortless voice melts with the music in every song she sings. Though don’t for one second think that effortless sound was not earned! After being taught guitar by her older brother, Hayley then spent many years training in voice, guitar and piano and honing her skills.",
        },
        {
          id: 2,
          name: "Bruno Major",
          day: "Thu",
          date: "23",
          month: "Apr",
          time: "9:00PM",
          location: "Live Stream Tour - Songs for Sydney",
          description:
            "Bruno Major splices classic singer/songwriter confessionals with sleek modern electronic production, girding the entire enterprise with hints of soul. ",
        },
      ],
    };
  },
  methods: {
    navigate() {
      this.$router.push("/events");
    },
    toEventPage(id) {
      this.$router.push({ name: "EventPage", params: { id: id } });
    },
  },
};
</script>

<style lang="scss">
.upcoming-list-wrap {
  margin-bottom: 20px;
  width: 100%;
  display: grid;
  grid-template-columns: 480px auto 480px;
  .v-item-group {
    grid-column: 2;
    width: auto;
    height: auto;
    background-color: transparent !important;
    .v-expansion-panel-header {
      margin-bottom: 45px;
      .item-date {
        height: 40px;
        width: 88px !important;
        margin-right: 10px !important;
        display: flex;
        align-items: center;
        &_left {
          margin: 10px;
          line-height: 40px;
          font-size: 40px;
          font-family: "Anton", sans-serif;
        }
        &_right {
          display: flex;
          flex-direction: column;
          align-items: center;
          line-height: 14px;
          font-size: 14px;
          font-family: "Anton", sans-serif;
          &_day {
            opacity: 0.5;
            margin: 5px;
            &_month {
              margin: 5px;
            }
          }
        }
      }
      .item-artist {
        margin-left: 20px;
        text-align: start !important;
        line-height: 28px;
        font-size: 28px;
        padding-top: 8px;
        font-family: "Anton", sans-serif;
      }
      .item-link {
        display: flex;
        justify-content: flex-end;
        .link-btn {
          outline: none;
          border: solid #fc9779 2px;
          background-color: transparent;
          color: #fc9779;
          font-size: 14px;
          text-align: start;
          line-height: 14px;
          font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
          padding: 13px 18px;
        }
      }
      &:hover {
        .item-artist {
          color: #fc9779;
        }
        .theme--light {
          .v-expansion-panels,
          .v-expansion-panel {
            border-bottom: solid #fc9779 1px;
          }
        }
      }
    }
    .v-expansion-panel-content {
      &__wrap {
        line-height: 1.5;
        font-size: 16px;
        font-weight: bold;
        font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
        margin-bottom: 50px;
      }
      .item-description {
        margin-top: 30px;
      }
    }
  }
  .theme--light {
    .v-expansion-panels,
    .v-expansion-panel {
      background-color: transparent !important;
      color: white !important;
      border-bottom: solid white 1px;
      margin-bottom: 45px;
    }
  }
  .v-expansion-panel-header__icon {
    display: none;
  }
}
</style>
