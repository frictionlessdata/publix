# Navigation

## Pages

This features provides an ability to create multi-page websites. The navigation menu will be available in the left column on the website and can be setup in the project config:

```yaml image
path: ../../assets/pages.png
width: 100%
height: unset
class: border
```

> livemark.yaml

```yaml
pages:
  items:
    - name: Introduction
      path: index
    - name: Getting Started
      items:
        - path: pages/getting-started/installation
        - path: pages/getting-started/configuration
```

## Topics

Livemark will automatically create a table of contents for every page on the website using this feature. It can be customized in the project config and the resulting section will be rendered in the left column on the website:

```yaml image
path: ../../assets/topics.png
width: 100%
height: unset
class: border
```

> livemark.yaml

```yaml
topics:
  selector: h2
```

## Links

Use this feature to add external links to the right column on the website:

```yaml image
path: ../../assets/links.png
width: 100%
height: unset
class: border
```

> livemark.yaml

```yaml
links:
  items:
    - name: Frictionless
      path: https://frictionlessdata.io
    - name: Discord
      path: https://discord.com/channels/695635777199145130/695635777199145133
    - name: Twitter
      path: https://twitter.com/frictionlessd8a
```

## Search

Ability to search is critical for a website. Livemark provides this feature out-of-box:

```yaml image
path: ../../assets/search.png
width: 100%
height: unset
class: border
```

## Signs

Livemark encourages book-reading experience in data journalism or documentation writing. This feature provides two buttons (previous/next page) at the bottom of every page.

```yaml image
path: ../../assets/signs.png
width: 100%
height: unset
class: border
```