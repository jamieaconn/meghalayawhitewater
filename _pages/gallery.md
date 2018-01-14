---
layout: page
title: Gallery
description: Gallery
sitemap:
    priority: 1.0
    lastmod: 2017-11-02
    changefreq: weekly
permalink: "/gallery/"
---



{% jekyllgram 6 %}
  <a href="{{ photo.link }}" title="{{ photo.caption.text }}">
    <img src="{{ photo.images.thumbnail.url }}" title="{{ photo.caption.text }}" />
  </a>
{% endjekyllgram %}